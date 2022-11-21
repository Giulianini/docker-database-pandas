import pymongo
import pandas as pd
from pymongo import MongoClient

client = MongoClient()

#point the client at mongo URI
client = MongoClient('Mongo URI')
#select database
db = client['database_name']
#select the collection within the database
collection = db['collection_name']
#convert entire collection to Pandas dataframe
df = pd.DataFrame(list(collection.find()))