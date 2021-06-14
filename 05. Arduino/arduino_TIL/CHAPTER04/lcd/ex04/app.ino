#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C myLCD(0x27, 16, 2);

uint8_t name_d[8] = {B11111, B10000, B10000, B11111, B00000, B00100, B00100, B11111};
uint8_t name_s[8] = {
        B00000,
        B00100,
        B00100,
        B00100,
        B01010,
        B10001,
        B00000,
        B00000
        };
uint8_t name_i[8] = {
        B00000,
        B01000,
        B01000,
        B01000,
        B01000,
        B01000,
        B01000,
        B00000
};
uint8_t name_y[8] = {
        B01001,
        B10111,
        B10111,
        B01001,
        B00101,
        B01010,
        B01010,
        B00100
};

void setup() {
  myLCD.begin();
  
  myLCD.createChar(0, name_d);
  myLCD.createChar(1, name_s);
  myLCD.createChar(2, name_i);
  myLCD.createChar(3, name_y);
}

void loop() {
  myLCD.setCursor(0,0);
  myLCD.print("Hello, Arduino!");

  myLCD.setCursor(0,1);
  myLCD.print("My name is ");
  
  myLCD.write(0);
  myLCD.write(1);
  myLCD.write(2);
  myLCD.write(3);
}