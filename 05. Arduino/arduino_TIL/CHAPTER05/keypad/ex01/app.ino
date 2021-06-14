#include <Keypad.h>
#include <MiniCom.h>
#include <SimpleTimer.h>
#include <Servo.h>
#include <EEPROM.h>
#include <Led.h>

Servo door;
MiniCom com;
SimpleTimer timer;
Led led(4);

const int servo_pin = 1;

const byte ROWS = 4;
const byte COLS = 4;

const byte col_pins[COLS] = {9,8,7,6};      // colum
const byte row_pins[ROWS] = {10,11,12,13};  // row

const char hex_keys[ROWS][COLS] = {
  {'0','1','2','3'},
  {'4','5','6','7'},
  {'8','9','A','B'},
  {'C','D','E','F'},
};

Keypad myKeypad = Keypad(makeKeymap(hex_keys), row_pins, col_pins, ROWS, COLS);
String input = "";
bool b_press = false;       //첫 번째 키 입력 여부
int timer_id;

String PASSWORD = "";

//키를 입력하면 input에 입력
// F키를 누르면 완료
// 입력한 문자열을 시리얼로 출력

String read_password() {
  String password = "";
  for(int i=0; i<20; i++) {
    char ch = EEPROM.read(i);
    if(ch == '\0') {
      break;
    }
    password += ch;
  }
  return password;
}
void write_password(String password) {
  int size = password.length();
  for(int i=0; i<size; i++) {
    char c = password[i];
    Serial.println(c);
    EEPROM.write(i,c);
  }
  EEPROM.write(size, '\0');
}

void beep(int interval=100) {
  led.on();
  delay(interval);
  led.off();
}

void reset() {
  Serial.println("Time out! reset");
  input = "";
  b_press = false;
  for(int i=0; i<3; i++){
    beep();
    delay(200);
  }
}

void open_door() {
  // 서보 모터로 문을 열어줌
  door.write(90);
  beep(200);

  delay(5000);
  // 서보 모터로 문을 닫아줌
  door.write(0);
  beep(200);
}


void setup() {
  // com.setInterval(100, check);
  Serial.begin(9600);
  door.attach(servo_pin);
  door.write(0);
  led.off();
  PASSWORD = read_password();
}

void loop() {
  timer.run();
  char key = myKeypad.getKey();

  if (key != NO_KEY){
    beep();
    if(key != 'F'){
      if(!b_press) {    // 첫 번째 키 입력 하면
        timer_id = timer.setTimeout(3000, reset);
        b_press = true;
      } else {
        timer.restartTimer(timer_id);
      }
      input += key;
    } else {
      timer.deleteTimer(timer_id);
      Serial.print("Input : ");
      Serial.println(input);

      if(input[0] == 'C') {
        PASSWORD = input.substring(1);
        write_password(PASSWORD);
        Serial.println("New Password: " + PASSWORD);
      } else {

        if(input == PASSWORD) {
          Serial.println("Password matched!");
          open_door();
        } else {
          Serial.println("Password Mismatched!");
          beep(1000);

        }
      }
      input = "";
      b_press = false;
    }
  }
}