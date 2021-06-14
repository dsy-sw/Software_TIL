#include <Led.h>

int pir_pin = 7;
Led led(8);

void setup() {
  pinMode(7,INPUT);
}

void loop() {
  int value = digitalRead(pir_pin);
  if(value == HIGH){
    led.on();
  } else {
    led.off();
  }
}