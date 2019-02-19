import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['paranuara']
collection_company = db['company']

with open('../resources/companies.json') as f:
    file_data = json.load(f)

collection_company.insert(file_data)

collection_people = db['people']

with open('../resources/people.json') as f:
    file_data = json.load(f)

collection_people.insert(file_data)

client.close()
