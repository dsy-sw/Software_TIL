// 스위치 풀업/풀다운 동작 확인
// 스위치 상태 그대로 풀업저항 연결 LED에 출력하기
#include <Led.h>

const int sw2 = 3;    // 풀다운 스위치 연결핀(sw2)
Led led1 = 9;    // 풀다운 스위치 확인용 LED(pull up)

const int sw1 = 4;
Led led2 = 8;

void setup() {
  pinMode(sw1, INPUT);
  pinMode(sw2, INPUT);
}

void loop() {
  int v1, v2;

  v1 = digitalRead(sw1);     // 풀업 스위치 상태 읽기
  led1.setValue(v1);      // 풀업 스위치 상태 LED 출력

  v2 = digitalRead(sw2);     // 풀업 스위치 상태 읽기
  led2.setValue(!v2);      // 풀업 스위치 상태 LED 출력
}