from kafka_facade import Kafka
from fastapi import FastAPI
import uvicorn
import threading

# shared state -- in-memory database using dictionaries
pid2cost = {}  # product IDs to unit cost
oid2order = {} # order IDs to order details
customer2orders = {}  # customer IDs to order IDs
date2oids = {} # date to sets of order IDs
lock = threading.Lock()

def update_order(order_id, order_details):
    # Check for mandatory fields
    customer_id = order_details.get('customer_id')
    if customer_id is None:
        print(f"Order {order_id} ignored: 'customer_id' is missing")
        return  # Exit if customer_id is not present
    
    new_date = order_details['date']
    
    with lock:
        old_order = oid2order.get(order_id, None)
        if old_order:
            old_date = old_order['date']
            if new_date != old_date:
                date2oids[old_date].remove(order_id)
        else:
            if new_date not in date2oids:
                date2oids[new_date] = set()
            date2oids[new_date].add(order_id)
            customer2orders.setdefault(customer_id, set()).add(order_id)
        oid2order[order_id] = order_details

def delete_order(order_id):
    with lock:
        old_order = oid2order.pop(order_id, None)
        if old_order:
            old_date = old_order['date']
            date2oids[old_date].remove(order_id)
            customer_id = old_order['customer_id']
            customer2orders[customer_id].remove(order_id)

def update_product(product_id, product):
    with lock:
        pid2cost[product_id] = product['unit_cost']

def delete_product(product_id):
    with lock:
        pid2cost.pop(product_id, None)

def calculate_profit_on(date):
    with lock:
        profit = 0
        for order_id in date2oids.get(date, set()):
            order = oid2order[order_id]
            for order_line in order['lines']:
                product_id = order_line['product']
                if product_id not in pid2cost:
                    print(f'Unknown product {product_id} ignored')
                    continue
                units = order_line['units']
                unit_price = order_line['unit_price']
                discount = order_line['discount']
                unit_cost = pid2cost[product_id]
                profit += units * (unit_price - unit_cost) - discount
        return profit

def get_customer_totals(customer_id):
    with lock:
        total_spent = 0
        if customer_id in customer2orders:
            for order_id in customer2orders[customer_id]:
                order = oid2order[order_id]
                for order_line in order['lines']:
                    total_spent += order_line['units'] * order_line['unit_price']
        return total_spent

def get_sales_per_category():
    with lock:
        category_sales = {}
        for order in oid2order.values():
            for order_line in order['lines']:
                category = order_line.get('category', 'Unknown')
                units = order_line['units']
                total_price = units * order_line['unit_price']
                category_sales[category] = category_sales.get(category, 0) + total_price
        return category_sales

def orders_consumer_loop():
    with Kafka('orders') as kafka:
        for message in kafka:
            print(f'order message received: {message}')
            if message.value is None:
                delete_order(message.key)
            else:
                update_order(message.key, message.value)

def products_consumer_loop():
    with Kafka('products') as kafka:
        for message in kafka:
            print(f'product message received: {message}')
            if message.value is None:
                delete_product(message.key)
            else:
                update_product(message.key, message.value)

def customers_consumer_loop():
    with Kafka('customers') as kafka:
        for message in kafka:
            print(f'customer message received: {message}')
            # Processing customer-related messages can be added here

# Web API
app = FastAPI()

@app.get('/api/profits_for_day/{date}')
def get_profits_by_day(date):
    return {'date': date, 'profit': round(calculate_profit_on(date), 2)}

@app.get('/api/customer_totals/{customer_id}')
def get_customer_total(customer_id):
    return {'customer_id': customer_id, 'total_spent': round(get_customer_totals(customer_id), 2)}

@app.get('/api/sales_per_category/')
def get_sales_by_category():
    return get_sales_per_category()

if __name__ == '__main__':
    orders_consumer_thread = threading.Thread(target=orders_consumer_loop, daemon=True)
    orders_consumer_thread.start()
    products_consumer_thread = threading.Thread(target=products_consumer_loop, daemon=True)
    products_consumer_thread.start()
    customers_consumer_thread = threading.Thread(target=customers_consumer_loop, daemon=True)
    customers_consumer_thread.start()
    uvicorn.run(app, host='0.0.0.0', port=3000)