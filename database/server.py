from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from typing import Dict
import os
import urllib.parse

load_dotenv()

username = urllib.parse.quote_plus(os.getenv("USER"))
password = urllib.parse.quote_plus(os.getenv("PASSWORD"))

connection = MongoClient("mongodb+srv://%s:%s@cluster0.gjsvusw.mongodb.net/?retryWrites=true&w=majority" % (username, password))

database = connection.dinoBaseDB
collection = database.dinosaurs

def delete_all():
    document = collection.delete_many({})
    return document.acknowledged

def delete_many(data: Dict):
    document = collection.delete_many(data)
    return 

def insert_many(data: Dict):
    document = collection.insert_many(data)
    return document.acknowledged

def insert_one(data: Dict):
    document = collection.insert_one(data)
    return document.acknowledged

def close_connection():
    connection.close()
