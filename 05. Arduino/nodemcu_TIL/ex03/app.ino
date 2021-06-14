#include <ESP8266WiFi.h>
#include <MiniCom.h>

const char *ssid = "DO";
const char *password = "ehtldud123";

MiniCom com(115200);

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

void setup() {
  com.init();

  wifi_connect();
}

void loop() {
  
}