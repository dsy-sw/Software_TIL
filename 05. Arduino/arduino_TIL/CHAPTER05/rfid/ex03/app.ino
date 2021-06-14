#include <SPI.h>
#include <MFRC522.h>
#include <Led.h>
#include <EEPROM.h>

#define RST_PIN 9
#define SS_PIN 10

Led led(8);
MFRC522 mfrc(SS_PIN, RST_PIN);
byte uid[4];


void read_uid() {
  for(int i=0; i<4; i++) {
    uid[i] = EEPROM.read(100+i);
    Serial.print(uid[i]);
    Serial.print(" ");
  }
  Serial.println();
}

bool check_uid(byte *target) {
  for(int i=0; i<4; i++) {
    if(uid[i] != target[i]) {
      return false;   // ID가 불일치하는 경우 false 리턴
    }
  }
  // ID가 일치하는 경우 true 리턴
  return true;
}

void beep(int interval=100) {
  led.on();
  delay(interval);
  led.off();
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

  //이번에 읽은 RFID 태그가 EEPROM에 저장된 값과 일치하는지 조사
  // 일치하면 서보모터로 문 열고, 않으면 긴 beep음 출력


  Serial.println();
}