#include <EEPROM.h>

int randomNumber;

void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(A0));
}

void loop() {
  for(int i=0; i<100; i++) {
    randomNumber = random(256);
    EEPROM.write(i, randomNumber);
    Serial.println(String(i));
    delay(100);
  }

  Serial.println();
  for(int i=0; i<100; i++) {
    randomNumber = EEPROM.read(i);
    Serial.print("EEPROM Address: ");
    Serial.print(String(i)+"\t");
    Serial.print("value: ");
    Serial.println(randomNumber);
    delay(100);
  }
  while(true);    // 한 번만
}