from mqtt_sub import subscribe
from pymongo import MongoClient
from datetime import datetime

db_client = MongoClient("mongodb://localhost:27017/")

iot_db = db_client['iot_service']
sensors_col = iot_db['sensors']

def on_message(client, userdate, msg):
  msg.payload = msg.payload.decode("utf-8")   # byte 데이터를 utf-8 문자열로 변환
  print(msg.topic + " " + str(msg.payload))

  sensor_value = {
    "topic" : msg.topic,
    "value" : float(msg.payload),
    "reg_date" : datetime.now()
  }
  sensors_col.insert_one(sensor_value)

subscribe('localhost', 'user1/home/#', on_message)