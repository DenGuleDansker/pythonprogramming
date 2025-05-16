from kafka_facade import Kafka
from fastapi import FastAPI
import uvicorn
import threading

# shared state -- in-memory database using dictionaries
pid2cost = {}  # product IDs to unit cost
oid2order = {} # order IDs to order details
date2oids = {} # date to sets of order IDs
lock = threading.Lock()

def update_order(order_id, order_details):
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
        oid2order[order_id] = order_details

def delete_order(order_id):
    with lock:
        old_order = oid2order.pop(order_id, None)
        if old_order:
            old_date = old_order['date']
            date2oids[old_date].remove(order_id)

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

# Web API
app = FastAPI()

@app.get('/api/profits_for_day/{date}')
def get_profits_by_day(date):
    return {'date': date, 'profit': round(calculate_profit_on(date), 2)}

if __name__ == '__main__':
    orders_consumer_thread = threading.Thread(target=orders_consumer_loop, daemon=True)
    orders_consumer_thread.start()
    products_consumer_thread = threading.Thread(target=products_consumer_loop, daemon=True)
    products_consumer_thread.start()
    uvicorn.run(app, port=3000)