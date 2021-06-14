#include <SimpleTimer.h>

const int var_pin = A0;
int analog_val;
SimpleTimer timer;

void setup() {
  Serial.begin(9600);
  timer.setInterval(100, check);
}

void check() {
  int digital_val;
  float ff;

  digital_val = analogRead(var_pin);      // 아날로그 값 디지털 변환

  ff = (float)digital_val / 1023. * 5.0;  // 전압값 계산

  Serial.print("Input Voltage(0~5V) = ");
  Serial.println(ff);                     // 변환된 디지털 값 출력(0~5V)

  Serial.print("Input Voltage(0~1023) = ");
  Serial.println(digital_val);            // 변환된 디지털 값 출력(0~1023)
  Serial.println("------------------------------");
}

void loop() {
  timer.run();
}