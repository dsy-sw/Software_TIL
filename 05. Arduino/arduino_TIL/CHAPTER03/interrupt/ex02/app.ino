#include <Led.h>
#include <Button.h>

Button btn(3);
Led led(8);


void flash() {
  if(btn.debounce()) {
    led.toggle();
  }
}

void setup() {
  btn.attachInterrupt(flash, FALLING);
}

void loop() {

}
