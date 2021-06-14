// 라이브러리 이용
#include <EEPROM.h>
#include <Keypad.h>
#include <SimpleTimer.h>
#include <Servo.h>
#include <Led.h>

const byte ROWS = 4;   // 4행
const byte COLS = 4;   // 4열

const byte col_pins[COLS] = {9, 8, 7, 6};   // 키패드 열 연결(C1~C4)
const byte row_pins[ROWS] = {10, 11, 12, 13};   // 키패드 행 연결(R1~R4) 

const char hex_keys[ROWS][COLS] = {       // 키 이름
  {'0','1','2','3'},
  {'4','5','6','7'},
  {'8','9','A','B'},
  {'C','D','E','F'}
};

Keypad myKeypad = Keypad(makeKeymap(hex_keys), row_pins, col_pins, ROWS, COLS);  // 키패드 객체 생성
String input="";
String PASSWORD = "";

bool b_press = false;   // 첫 번째 입력인지 여부 판단.
SimpleTimer timer;
int timer_id;

Servo door;
Led led(4); // 부저와 같이 동작 

String read_password() {
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

void write_password(String password) {
    int size = password.length();   // 문자열 길이 
    for(int i=0; i < size; i++) {
        char c = password[i];   
        EEPROM.write(i, c);     
    }
    EEPROM.write(size, '\0');   // 문자열의 끝 기록
}

// 키 입력을 하면 input에 구성
// F를 누르면 완료... 
// 이때까지 입력한 문자열을 
// 시리얼로 출력

void setup() {
  Serial.begin(9600);
  door.attach(5);
  door.write(0);
  led.off();
  PASSWORD = read_password();   // 저장된 비밀번호 읽어오기
}

void beep(int interval = 100) {
    led.on();
    delay(interval);
    led.off();
}

void reset() {
    Serial.println("time out ! reset");
    input = "";
    b_press = false;
    for(int i=0; i< 3; i++) {
        beep();
        delay(200);
    }
}

void open_door() {
    // 서보 모터로 문을 열어줌.
    beep(200);
    door.write(90);
    delay(5000);
    // 서보 모터로 문을 닫음.
    door.write(0);
    beep(200);
}


void loop()
{
  timer.run();
  char key = myKeypad.getKey();
     
  if(key != NO_KEY){          // 시리얼 모니터 눌린 키 이름 출력 
    beep();
    if(key != 'F') {    // 키 입력 중
        if(!b_press) {  // 첫 번째 키 입력이면...
            // 타이머 setTimeout
            timer_id = timer.setTimeout(3000, reset);
            b_press = true;
        } else {    //
            // 타이머 restart
            timer.restartTimer(timer_id);
        }
        input += key;
    } else {    // 키 입력이 완료됨
        timer.deleteTimer(timer_id);
        Serial.print("Input: ");
        Serial.println(input);  

        // 'C'로 시작하면 새로운 비밀번호 저장
        // 'C0248' 이면 '0248'이 새로운 비밀번호가 됨.
        if(input[0] == 'C') {
            PASSWORD = input.substring(1); // substring(from, to) to는 미포함
            write_password(PASSWORD);
            Serial.println("New Password: " + PASSWORD);
        } else {
            if(input == PASSWORD) {
                // 문을 열러줌.
                Serial.println("Password Matched!");
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

