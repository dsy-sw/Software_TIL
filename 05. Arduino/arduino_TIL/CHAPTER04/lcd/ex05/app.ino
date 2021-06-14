#include <LiquidCrystal_I2C.h>
#include <SimpleTimer.h>

const int var_pin = A0;       // 가변저항 연결핀
int analog_val;               // 아날로그 값 저장 변수
SimpleTimer timer;
LiquidCrystal_I2C myLCD(0x27, 16, 2);

void check(){
  int digital_var;
  float ff;
  digital_var = analogRead(var_pin);
  ff = (float)digital_var / 1023. * 5.;

  // myLCD.clear();

  char msg[17];

  String buf = "volt: ";
  buf = buf + ff +"V";
  sprintf(msg, "%-16s", buf.c_str());
  myLCD.setCursor(0,0);
  // myLCD.print(buf.c_str());
  myLCD.print(msg);

  buf = "D.value: ";
  buf = buf + digital_var;
  sprintf(msg, "%-16s", buf.c_str());
  sprintf(msg, "d.value: %d", digital_var);
  myLCD.setCursor(0,1);
  // myLCD.print(buf.c_str());
  myLCD.print(msg);
}
void setup() {
  Serial.begin(9600);
  myLCD.begin();
  timer.setInterval(100,check);
}

void loop() {
  timer.run();
}