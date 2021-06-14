// 버튼을 누른 후 5초 동안만 아날로그 값 측정
// 이 기간동안 LED는 켜짐
// 5초 후 LED 꺼지고, 값은 측정되지 않음.

#include <Led.h>
#include <SimpleTimer.h>
#include <Button.h>

const int var_pin = A0;

Button btn(3);
Led led(8);
SimpleTimer timer;

int timerId = -1;


void start() {
  if(!btn.debounce()) return;

  if(timerId == -1) {
  led.on();
  timerId = timer.setInterval(100, check);    // 0.1초 간격 타이머 시작
  timer.setTimeout(5000, stop);               // 5초 후 타임아웃 stop 호출
  } else{ 
  stop();   
  }

}

void stop() {
  led.off();
  timer.deleteTimer(timerId);   // 측정 타이머 제거
  timerId = -1;
}

void setup() {
  Serial.begin(9600);
  btn.attachInterrupt(start, FALLING);
}

void loop() {
  timer.run();
}

void check() {
  int digital_val;
  float ff;

  digital_val = analogRead(var_pin);      // 아날로그 값 디지털 변환

  ff = (float)digital_val / 1023. * 5.0;  // 전압값 계산

  Serial.print("Input Voltage(0~5V) = ");
  Serial.println(ff);                     // 변환된 디지털 값 출력(0~5V)

  Serial.print("Input Voltage(0~1023) = ");
  Serial.println(digital_val);            // 변환된 디지털 값 출력(0~1023)
  Serial.println("------------------------------");
}