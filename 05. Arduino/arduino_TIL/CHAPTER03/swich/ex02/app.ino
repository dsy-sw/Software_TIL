#include <Led.h>

Led led(8);
int sw=4;

void setup() {
  pinMode(sw, INPUT_PULLUP);
}

void loop() {
  int v = digitalRead(sw);
  led.setValue(!v);
}