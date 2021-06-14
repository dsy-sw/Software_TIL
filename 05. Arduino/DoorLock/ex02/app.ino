#include <Keypad.h>
#include <SimpleTimer.h>
#include <DoorLock.h>


DoorLock dl;
SimpleTimer timer;
bool b_press = false;   // 첫 번째 입력인지 여부 판단.
int timer_id;

String input="";
String PASSWORD = "";

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

void reset() {
    Serial.println("time out ! reset");
    input = "";
    bool b_press = false;
    for(int i=0; i< 3; i++) {
        dl.beep();
        delay(200);
    }
}

void setup() {
  dl.init();
}

void loop()
{
  timer.run();
  char key = myKeypad.getKey();
     
  if(key != NO_KEY){          // 시리얼 모니터 눌린 키 이름 출력 
    dl.beep();
    if(key != 'F') {    // 키 입력 중
        if(!b_press) {  // 첫 번째 키 입력 시
            // 타이머 setTimeout
            timer_id = timer.setTimeout(3000, reset);
            b_press = true;
        } else {    //
            // 타이머 restart
            timer.restartTimer(timer_id);
        }
        input += key;
    } else {    // 키 입력 완료 시
        timer.deleteTimer(timer_id);
        Serial.print("Input: ");
        Serial.println(input);  

        // 'C'로 시작하면 비밀번호 변경 후 저장
        if(input[0] == 'C') {
            PASSWORD = input.substring(1);
            dl.write_password(PASSWORD);
            Serial.println("New Password: " + PASSWORD);
        } else {
            if(input == PASSWORD) {
                // 문을 열러줌.
                Serial.println("Password Matched!");
                dl.open_door();
            } else {
                Serial.println("Password Mismatched!");
                dl.beep(1000);
            }
        }
        input = "";
        b_press = false;
    }
  }
}

