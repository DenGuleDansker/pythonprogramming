from kafka_facade import Kafka

with Kafka('orders') as kafka:
    kafka.send('o-1245', {
        'customer': 'c-45',
        'date': '2025-05-13',
        'lines': [{
            'product': 'p-245',
            'units': 12,
            'unit_price': 17.00,
            'discount': 24.00,
        },{
            'product': 'p-109',
            'units': 50,
            'unit_price': 42.50,
            'discount': 0.00,
        }],
    })
    kafka.send('o-124567', {
        'customer': 'c-45',
        'date': '2025-05-13',
        'lines': [{
            'product': 'p-245',
            'units': 12,
            'unit_price': 17.00,
            'discount': 24.00,
        },{
            'product': 'p-109',
            'units': 50,
            'unit_price': 42.50,
            'discount': 0.00,
        }],
    })
    kafka.send('o-2278', {
        'customer': 'c-47',
        'date': '2025-05-14',
        'lines': [{
            'product': 'p-328',
            'units': 6,
            'unit_price': 300.00,
            'discount': 200.00,
        }],
    })
    kafka.start_interactive_producer_loop()