#include <EEPROM.h>

String password = "";

void setup() {    // EEPROM에서 읽어서 password에 복원
  for(int i=0; i<100;i++) {
    char ch = EEPROM.read(i);
    if(ch == '\0') {
      break;
    }
    password += ch;
  }

  Serial.println("password: " + password);
}

void loop() {

}