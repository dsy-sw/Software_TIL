#include <SPI.h>
#include <MFRC522.h>
#include <Led.h>
#include <EEPROM.h>

#define RST_PIN 9
#define SS_PIN 10

Led led(8);
MFRC522 mfrc(SS_PIN, RST_PIN);

void write_uid(byte *uid){
  for(int i=0; i<4; i++) {
    EEPROM.write(100+i, uid[i]);
  }
}

void setup() {
  Serial.begin(9600);
  SPI.begin();
  mfrc.PCD_Init();
}

void loop() {
  if(!mfrc.PICC_IsNewCardPresent() || !mfrc.PICC_ReadCardSerial()) {
    delay(500);
     return;
  }
  led.on();
  delay(100);
  led.off();
  Serial.print("Card UID: ");

  for(byte i=0; i<4; i++) {
    Serial.print(mfrc.uid.uidByte[i]);
    Serial.print(" ");
  }
  write_uid(mfrc.uid.uidByte);
  Serial.println();
}