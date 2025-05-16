import random
import csv

def generate_csv_file(file_name, row_count):
    random.seed(0)
    product_ids = [
        'b-003', 'b-184', 'b-049', 'b-207', 'b-090', 'b-226', 'b-001', 'b-103',
        'b-308', 'b-062', 'b-033', 'b-214', 'b-182', 'b-017', 'b-340', 'b-162',
        'b-157', 'b-203', 'b-078', 'b-009',
    ]
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(('date', 'product ID', 'units'))
        i = 0
        while i < row_count:
            month = random.randint(1, 12)
            day_count = 29 if month == 2 else 30 if month in (4, 6, 9, 11) else 31
            day = random.randint(1, day_count)
            date = f'{2024}-{month:0>2}-{day:0>2}'
            product_id = random.choice(product_ids)
            units = random.randint(1, 10)
            writer.writerow((date, product_id, units))
            i += 1

if __name__ == '__main__':
    import sys
    generate_csv_file(sys.argv[1], int(sys.argv[2]))