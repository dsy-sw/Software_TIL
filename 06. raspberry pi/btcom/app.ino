// 1. Joystick의 값을 읽어서 LCD에 출력
// 2. Bluetooth로 x, y값을 라즈베리파이에 전송

#include <BtMiniCom.h>
#include <Button.h>
#include <ArduinoJson.h>

void receive(String msg) {

}

Button btn(2);
BtMiniCom com(11, 12, receive);

void capture() {
  // if(!btn.debounce()) return;
  String msg;
  StaticJsonDocument<128> doc;
  doc["target"] = "camera";
  doc["camera"] = "capture";
  serializeJson(doc, msg);
  // Serial.println(msg);
  com.send(msg);
}

void check() {
  int x = analogRead(A1);
  int y = analogRead(A0);
  // 0~ 1023 -> -90 ~ 90
  x = map(x, 0, 1023, -90, 90);
  y = map(y, 0, 1023, -90, 90);
  com.print_i(0,"X: ", x);
  com.print_i(1,"Y: ", y);

  // 블루투스로 전송
  String msg;
  // json 문자열로 전송
  StaticJsonDocument<128> doc;
  doc["target"] = "servo";
  doc["x"] = x;
  doc["y"] = y;
  serializeJson(doc,msg);
  // Serial.println(msg);
  
  com.send(msg);
}

void setup()
{
	com.init();
  com.setInterval(500, check);
  // btn.attachInterrupt(caputure, FALLING);
  btn.setCallback(capture);
}

void loop()
{
	com.run();
  btn.check();
}
