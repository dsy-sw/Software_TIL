import paho.mqtt.client as mqtt

def subscribe(host, topic, on_message, forever=True):
  def on_connect(client, userdata, flasgs, rc):
    print(f"Connected with result code {rc}")
    if rc == 0:
      client.subscribe(topic)
    else:
      print('연결 실패 : ', rc)

  client = mqtt.Client()

  client.on_connect = on_connect
  client.on_message = on_message
  client.connect(host)

  if forever:
    client.loop_forever()
  else:
    client.loop_start()