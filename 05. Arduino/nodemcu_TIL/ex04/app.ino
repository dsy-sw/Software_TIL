#include <ESP8266WiFi.h>
#include <MiniCom.h>
#include <PubSubClient.h>

const char *ssid = "DO";
const char *password = "ehtldud123";
const char* mqtt_server = "218.38.254.30";

MiniCom com(115200);
WiFiServer server(80);

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;

void wifi_connect() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  com.print(0, "Wifi connected", true);
  IPAddress ip = WiFi.localIP();
  String ipstr = ip.toString();
  com.print(1, ipstr.c_str(), true);
}
void callback(char *topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i=0; i<length; i++){
    Serial.print((char)payload[i]);
  }
  Serial.println();

  if((char)payload[0] == '1') {
    digitalWrite(BUILTIN_LED, LOW);
  } else {
    digitalWrite(BUILTIN_LED, HIGH);
  }
}

void reconnect() {
  // Loop until we're reconnected
  while(!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if(client.connect("ESP8266Client")) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("outTopic", "hello world");
      // ... and resubscribe
      client.subscribe("inTopic");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup() {
  com.init();
  WiFi.mode(WIFI_STA);
  pinMode(BUILTIN_LED, OUTPUT);
  wifi_connect();
  server.begin(115200);
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);       // subscribe 수신 시 호출할 함수 등록
}

void loop() {
  if (!client.connected()){
    reconnect();
  }
  client.loop();

  long now = millis();
  if(now - lastMsg > 2000) {  // 2초 간격으로 publish
    lastMsg = now;
    ++value;
    snprintf(msg, 75, "hello world #%ld", value);
    Serial.print("Publish message: ");
    Serial.println(msg);
    client.publish("outTopic", msg);
  }

  // Serial.println("server accept...");
  WiFiClient client = server.available();
  if(!client) {
    return;
  }

  Serial.println("new client");
  while (!client.available()) {
    delay(1);
  }

  String request = client.readStringUntil('\r');
  Serial.println(request);
  client.flush();

  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/html");
  client.println("");     // 잊지 말기 / 빈 줄 --> head와 body를 구분하는 역할
  client.println("<!DOCTYPE HTML>");
  client.println("<html>");
  client.println("HELLO WORLD!");
  client.println("</html>");
  delay(1);
  client.println("Client disconnected");
  client.println("");
}