#include <Button.h>

Button btn(3);
int state = LOW;

void work() {
  if(btn.debounce()) return;
  state = !state;
  digitalWrite(9, state);
}

void setup() {
  pinMode(9, OUTPUT);
  btn.attachInterrupt(work, FALLING);
}

void loop() {
  
}