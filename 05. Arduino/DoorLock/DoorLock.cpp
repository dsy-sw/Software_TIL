#include <DoorLock.h>


DoorLock::DoorLock(int led_pin)
  : led(led_pin){
}

String DoorLock::read_password() {
    String password = "";
    for(int i=0; i < 20; i++) {
        char ch = EEPROM.read(i);
        if(ch == '\0') {    // 문자열의 끝이면 중지
            break;
        }
        password += ch;
    }
    return password;
}

void DoorLock::init() {
  String PASSWORD = "";
  Serial.begin(9600);
  door.attach(5);
  door.write(0);
  PASSWORD = read_password();   // 저장된 비밀번호 읽어오기
  led.off();

}

void DoorLock::write_password(String password) {
    int size = password.length();   // 문자열 길이 
    for(int i=0; i < size; i++) {
        char c = password[i];   
        EEPROM.write(i, c);     
    }
    EEPROM.write(size, '\0');   // 문자열의 끝 기록
}

void DoorLock::beep(int interval) {
    led.on();
    delay(interval);
    led.off();
}

// void DoorLock::reset() {
//     Serial.println("time out ! reset");
//     input = "";
//     bool b_press = false;
//     for(int i=0; i< 3; i++) {
//         beep();
//         delay(200);
//     }
// }

void  DoorLock::open_door() {
    // 서보 모터로 문을 열어줌.
    beep(200);
    door.write(90);
    delay(5000);
    // 서보 모터로 문을 닫음.
    door.write(0);
    beep(200);
}