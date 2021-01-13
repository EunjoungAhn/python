# Requires pymongo 3.6.0+
from pymongo import MongoClient

client = MongoClient("mongodb://cluster0.aibnd.mongodb.net:27017/")
database = client["mega202101"]
collection = database["member"]

# Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

query = {'name':'park'}

cursor = collection.find(query)
print(cursor)

try:
    for doc in cursor:
        print(doc)
finally:
    client.close()
