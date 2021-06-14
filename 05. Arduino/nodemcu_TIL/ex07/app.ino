#include <MqttCom.h>
#include <DHT.h>
#include <PWMLed.h>
#include <ArduinoJson.h>

const char *ssid = "DO";
const char *password = "ehtldud123";
const char *server =  "218.38.254.30";
const char *sub_topic = "test/led";

MqttCom com(ssid, password);
DHT dht11(D5, DHT11);
PWMLed led(D6);

void subscribe(char* topic, uint8_t* payload, unsigned int length) {
  char buf[128];
  memcpy(buf, payload, length);
  buf[length] = '\0';

  // JSON 문자열 -> 객체로 변환
  StaticJsonDocument<128> doc;
  auto error = deserializeJson(doc, buf);
  if(error){
    Serial.println("deserializeJson() error");
    Serial.println(error.c_str());
    return;
  }

  const char *device = doc["deivce"];
  int value = doc["value"].as<int>();

  Serial.println(topic);
  Serial.println(buf);

  // int value = atoi(buf);   // atoi(aski to integer) : 문자열을 int로 변환
                            // atof(aski to float) : 문자열을 double로 변환
  led.setValue(value);
}

void publish() {
  double temp = dht11.readTemperature();
  double humi = dht11.readHumidity();
  com.print_d(0, "Temp. : ", temp);
  com.print_d(1, "Humi. : ", humi);

  String value ="";
  value+= temp;
  com.publish("user1/home/livingroom/temp", value.c_str());
  value="";
  value+=humi;
  com.publish("user1/home/livingroom/humi", value.c_str());
}

void setup() {
  // com.init(server);    // publish만 하는 경우
  com.init(server, sub_topic, subscribe);   // subscribe하는 경우
  com.setInterval(2000, publish);
}

void loop() {
  com.run();
}