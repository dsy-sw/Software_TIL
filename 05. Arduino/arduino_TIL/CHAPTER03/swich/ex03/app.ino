#include <Led.h>

Led led(8);
int sw=4;

void setup() {
  pinMode(sw, INPUT_PULLUP);
}

void loop() {
  bool o_sw, n_sw;
  
  o_sw = digitalRead(sw);
  delay(10);
  n_sw = digitalRead(sw);

  if(o_sw == 1 && n_sw == 0){     // 버튼을 누른 시점
    led.toggle();
  }
}