import csv
import json

def check_reader_data(data):
    for row in data:
            try:
                row['Lat'] = float(row['Lat'])
                row['Long'] = float(row['Long'])
                row['Altitude'] = float(row['Altitude'])
            except Exception as exp:
                raise ValueError(str(exp))
    return data

def csv_reader(file_location):
    with open(file_location, mode='r') as csv_file:
        data = [line for line in csv.DictReader(csv_file)]
        return check_reader_data(data)

def json_reader(file_location):
    with open(file_location, mode='r') as json_file:
        data = json.loads(json_file.read())
        return check_reader_data(data)