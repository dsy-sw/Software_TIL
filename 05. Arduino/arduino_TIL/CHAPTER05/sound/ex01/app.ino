#include <MiniCom.h>

MiniCom com;
int count = 0;

void check() {
  int level = analogRead(A0);
  com.print_i(0, "Sound: ", level);
}

void setup() {
  com.init();
  com.setInterval(1000, check);
}

void loop() {
  com.run();
}