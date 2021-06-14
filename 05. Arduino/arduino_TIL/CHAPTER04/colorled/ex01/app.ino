#include <Led.h>

Led red(9), green(10), blue(11);

void setup()
{
	
}

void loop()
{
	one_color();
	two_color();
	full_color();
  
}

void led_off() {
  red.off();
  green.off();
  blue.off();
}

void one_color() {
  red.on();
  delay(2000);
  red.off();
  
  green.on();
  delay(2000);
  green.off();

  blue.on();
  delay(2000);
  blue.off();
}

void two_color() {
  red.on();
  green.on();
  delay(2000);
  red.off();
  green.off();
  
  green.on();
  blue.on();
  delay(2000);
  green.off();
  blue.off();

  red.on();
  blue.on();
  delay(2000);
  blue.off();
  red.off();
}

void full_color() {
  red.on();
  green.on();
  blue.on();
  delay(2000);
  red.off();
  green.off();
  blue.off();
}