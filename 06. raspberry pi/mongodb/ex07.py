from pymongo import MongoClient
from datetime import datetime
import random

db_client = MongoClient("mongodb://localhost:27017/")
iot_db = db_client['iot_service']
sensors_col = iot_db['sensors']

query = {"value" : {"$gt":55.1}}
rows = sensors_col.find(query).sort("value")   # 내림차순.sort("valuem", -1)

for x in rows:
  print(x)