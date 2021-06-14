#include <MiniCom.h>

MiniCom com;

void check() {
  int digital_val = analogRead(A0);
  Serial.println("check called");
  float ff = (float)digital_val / 1023. *5.0;

  com.print_d(0, "Volt: ", ff, false);
  com.print_i(1, "D.value:", digital_val, true);
}

void setup() {
  com.init();
  com.setInterval(100, check);
}

void loop() {
  com.run();
}