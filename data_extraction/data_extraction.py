from database import server
import csv

uri = 'data\data.csv'

with open(uri, 'r') as data:
    dinos = csv.DictReader(data)
    server.insert_multiple_data(dinos)

server.close_connection()