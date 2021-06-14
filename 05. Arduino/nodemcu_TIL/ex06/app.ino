#include <MqttCom.h>

const char *ssid = "DO";
const char *password = "ehtldud123";
const char *server =  "218.38.254.30";
const char *sub_topic = "test/led";

MqttCom com(ssid, password);

void publish() {
  com.publish("test/greet", "Hello world!");
}

void subscribe(char* topic, uint8_t* payload, unsigned int length) {
  char buf[128];
  memcpy(buf, payload, length);
  buf[length] = '\0';

  Serial.println(topic);
  Serial.println(buf);
}

void setup() {
  // com.init(server);    // publish만 하는 경우
  com.init(server, sub_topic, subscribe);   // subscribe하는 경우
  com.setInterval(2000, publish);
}

void loop() {
  com.run();
}