#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C myLCD(0x27, 16, 2);   // myLCD 객체 생성

void setup() {
  myLCD.begin();

  myLCD.setCursor(0,0);
  myLCD.print("I2C LCD Test!");

  myLCD.setCursor(0,1);
  myLCD.print("Hello, Arduino");
}

void loop() {

}