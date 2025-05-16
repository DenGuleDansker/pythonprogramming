from kafka_facade import Kafka

with Kafka('orders') as kafka:
    kafka.send('o-101', {
        'customer_id': 'c-45',  # Reference to the customer ID
        'date': '2023-10-01',
        'lines': [
            {'product': 'p-1', 'units': 10, 'unit_price': 100, 'discount': 0},
            {'product': 'p-2', 'units': 5, 'unit_price': 80, 'discount': 5},
        ]
    })
    
    kafka.send('o-102', {
        'customer_id': 'c-47',
        'date': '2023-10-02',
        'lines': [
            {'product': 'p-3', 'units': 2, 'unit_price': 150, 'discount': 10},
        ]
    })
    
    kafka.start_interactive_producer_loop()