#include <EEPROM.h>

String password = "123456";

void setup() {
  int size = password.length();
  for(int i=0; i<size; i++) {
    char c = password[i];
    Serial.println(c);
    EEPROM.write(i, c);
  }
  EEPROM.write(size, '\0');   // 문자열의 끝
}

void loop() {

}