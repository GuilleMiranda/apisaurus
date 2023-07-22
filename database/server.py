from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import urllib.parse
from bson import ObjectId

load_dotenv()

username = urllib.parse.quote_plus(os.getenv("USERNAME"))
password = urllib.parse.quote_plus(os.getenv("PASSWORD"))

connection = MongoClient("mongodb+srv://%s:%s@cluster0.gjsvusw.mongodb.net/?retryWrites=true&w=majority" % (username, password))

database = connection.dinoBaseDB
collection = database.dinosaurs


def insert_data(data):
    document = collection.insert_one(data)
    return document.acknowledged

def insert_multiple_data(data):
    document = collection.insert_many(data)
    return document.acknowledged

def close_connection():
    connection.close()
