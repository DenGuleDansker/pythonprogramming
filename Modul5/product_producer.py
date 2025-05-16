from kafka_facade import Kafka

with Kafka('products') as kafka:
    kafka.send('p-245', {
        'name': '6mm staples',
        'category': 'stationary',
        'unit': '1000pcs box',
        'unit_cost': 4.52,
    })
    kafka.send('p-328', {
        'name': 'The Boss Ergonomic office chair',
        'category': 'office furniture',
        'unit': 'pcs',
        'unit_cost': 10.85
    })
    kafka.send('p-109', {
        'name': 'Lavazza whole beans coffee',
        'category': 'pantry supplies',
        'unit': 'kg',
        'unit_cost': 24.77
    })
    kafka.start_interactive_producer_loop()