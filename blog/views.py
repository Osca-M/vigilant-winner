from django.shortcuts import render
from pymongo import MongoClient
# Create your views here.
USERNAME = 'vigilante'
PASSWORD = 'sirikuu'
DATABASE_HOST = 'localhost'
DATABASE_NAME = 'vigilant-winner'
connection_string = f'mongodb+srv://{USERNAME}:{PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}?retryWrites=true&w=majority'
client = MongoClient(connection_string)
db = client['db_name']
print(db, 'db')


