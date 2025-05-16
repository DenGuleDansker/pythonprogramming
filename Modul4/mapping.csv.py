import csv

def stream_from_csv(file_name):
    with open(file_name) as file:
        reader = csv.reader(file)
        next(reader) # skip header
        for row in reader:
            yield row



