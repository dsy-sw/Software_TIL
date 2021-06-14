#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C myLCD(0x27, 16, 2);

void setup() {
  myLCD.begin();

  myLCD.setCursor(0,0);
  myLCD.print("1+++++++23--------45*********67#######8");

  myLCD.setCursor(0,1);
  myLCD.print("1+++++++23--------45*********67#######8");
}

void loop() {
  int n;
  for(n=0; n<80; n++) {
    myLCD.scrollDisplayLeft();
    delay(500);
  }
  delay(2000);
  for(n=0; n<80; n++) {
    myLCD.scrollDisplayRight();
    delay(500);
  }
  delay(2000);
}