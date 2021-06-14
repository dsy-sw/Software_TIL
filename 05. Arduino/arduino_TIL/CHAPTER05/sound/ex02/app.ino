#include <MiniCom.h>

int count = 0;
MiniCom com;

void check() {
  int value = digitalRead(8);
  if(value == HIGH) {
    count++;
  }
}

void print() {
  com.print_i(0, "detect: ", count, true);
  count = 0;
}

void setup() {
  com.init();
  com.setInterval(100, check);
  com.setInterval(1000, print);
}

void loop () {
  com.run();
}