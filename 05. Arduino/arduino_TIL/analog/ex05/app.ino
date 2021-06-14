#include <PWMLed.h>

PWMLed led(9);

void setup() {

}

void loop() {
  int a_val, pwm_val;
  a_val = analogRead(A0);
  pwm_val = map(a_val, 0, 1023, 255, 0);

  led.setValue(pwm_val);
}