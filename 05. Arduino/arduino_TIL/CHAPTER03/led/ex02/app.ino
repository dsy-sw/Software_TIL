// LED 풀업/풀다운 연결핀 HIGH 출력 확인
const int led1_pin = 4;   // 
const int led2_pin = 5;   // 
const int led3_pin = 6;   // 
const int led4_pin = 7;   // 


void setup() {
pinMode(led1_pin, OUTPUT);    // 4번 핀 출력 설정
pinMode(led2_pin, OUTPUT);    // 4번 핀 출력 설정
pinMode(led3_pin, OUTPUT);    // 4번 핀 출력 설정
pinMode(led4_pin, OUTPUT);    // 4번 핀 출력 설정

}

void loop() {
  // led1만 on
digitalWrite(led1_pin, HIGH);   // 4번 핀 low 출력(on)
digitalWrite(led2_pin, LOW);   // 5번 핀 low 출력(off)
digitalWrite(led3_pin, LOW);   // 6번 핀 low 출력(off)
digitalWrite(led4_pin, LOW);   // 7번 핀 low 출력(off)
delay(100);

  // led2만 on
digitalWrite(led1_pin, LOW);   // 4번 핀 low 출력(off)
digitalWrite(led2_pin, HIGH);   // 5번 핀 low 출력(on)
digitalWrite(led3_pin, LOW);   // 6번 핀 low 출력(off)
digitalWrite(led4_pin, LOW);   // 7번 핀 low 출력(off)
delay(100);

  // led3만 on
digitalWrite(led1_pin, LOW);   // 4번 핀 low 출력(off)
digitalWrite(led2_pin, LOW);   // 5번 핀 low 출력(off)
digitalWrite(led3_pin, HIGH);   // 6번 핀 low 출력(on)
digitalWrite(led4_pin, LOW);   // 7번 핀 low 출력(off)
delay(100);

  // led4만 on
digitalWrite(led1_pin, LOW);   // 4번 핀 low 출력(off)
digitalWrite(led2_pin, LOW);   // 5번 핀 low 출력(off)
digitalWrite(led3_pin, LOW);   // 6번 핀 low 출력(off)
digitalWrite(led4_pin, HIGH);   // 7번 핀 low 출력(on)
delay(100);

}