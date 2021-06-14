#include <Led.h>
#include <MiniCom.h> 
#include <Button.h> 

Led led(8);
Button btn(A2);
MiniCom com;



void check() {
  int x = analogRead(A1);
  int y = analogRead(A0);
  x = map(x, 0, 1023, -255, 255);
  y = map(y, 0, 1023, 255, -255);
  com.print_i(0,"X: ",x);
  com.print_i(1,"Y: ",y);
}

void blink() {
  led.toggle();
}

void setup() {
  com.init();
  com.setInterval(100,check);
  // btn.attachInterrupt(blink, FALLING);
  btn.setCallback(blink);
}

void loop() {
  com.run();
  btn.check();
}