import paho.mqtt.client as mqtt
import json

# 1. MQTT 클라이언트 객체 인스턴스화
client = mqtt.Client()

def publish(topic, device, value):
  dic = {
    "device" : device,
    "value" : value
  }
  client.publish(topic, json.dumps(dic))

try:
  # 2. 브로커 연결
  client.connect("localhost")
  client.loop_start()     # 새로운 쓰레드(데몬 스레드)로 실행 - 메시지 처리
  while True:
    ans = input('밝기: ')
    if ans == 'q':
      break
    value = int(ans)
    publish('test/led', 'led', value)


except Exception as err:
  print('에러 : %s'%err)