#include <BtMiniCom.h>
#include <Robot.h>

void receive(String msg);

Robot car(8, 7, 9, 5, 4, 3);
BtMiniCom com(10, 11, receive);

void receive(String msg) {
  com.print(0, "Command: ");
  com.print(1, msg.c_str());
  
  if(msg=="f") {
    car.forward();
  } else if(msg=="b") {
    car.backward();
  } else if(msg=="s") {
    car.stop();
  } else if(msg=="r") {
    car.turn_right();
  } else if(msg=="l") {
    car.turn_left();
  } else {
    com.send("Unknown Command");
  }
}


void setup() {
  com.init();
  car.stop();
  car.setSpeed(200);
}

void loop() {
  com.run();
}