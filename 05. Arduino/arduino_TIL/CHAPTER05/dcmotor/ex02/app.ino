#include <Robot.h>

Robot car(8, 7, 9, 5, 4, 3);

void setup() {
  car.stop();
  car.setSpeed(200);  
}

void loop() {
  car.forward();
  delay(500);
  car.stop();
  delay(500);

  car.backward();
  delay(500);
  car.stop();
  delay(500);

  car.turn_left();
  delay(500);
  car.stop();
  delay(500);

  car.turn_right();
  delay(500);
  car.stop();
  delay(500);
}
