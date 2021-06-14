#include <PWMLed.h>

PWMLed led(9);

void setup() {
  // pinMode(led(9), OUTPUT);
  // digitalWrite(led(9), 0);
}

void loop() {
  int pwm_val;

  for (pwm_val = 0; pwm_val < 256; pwm_val +=5) {
    // analogWrite(led(9), pwm_val);    // PWM 신호 출력
    delay(100);
  }

  led.off();
  // digitalWrite(led(9), 0);   // LED OFF
  delay(2000);                // 2초 대기
}