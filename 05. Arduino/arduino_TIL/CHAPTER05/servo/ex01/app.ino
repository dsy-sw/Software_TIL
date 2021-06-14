#include <Servo.h>
#include <MiniCom.h>

Servo myServo;
MiniCom com;

const int servo_pin = 9;

void control() {
  int var = analogRead(A1);
  int angle = map(var, 0, 1023, 0, 180);
  myServo.write(angle);
  com.print_i(0, "Angle: ", angle-90);
  delay(1000);
}

void setup() {
  com.init();
  com.setInterval(100, control);
  myServo.attach(servo_pin);
}

void loop() {
  com.run();
}