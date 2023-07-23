# Local
from database import server

# External
import csv

uri = 'data\data.csv'

server.delete_all()

with open(uri, 'r') as data:
    dinos = csv.DictReader(data)
    if (server.insert_many(dinos)):
        print("Operación exitosa.")
    else:
        print("Ocurrió un error")
    

server.close_connection()