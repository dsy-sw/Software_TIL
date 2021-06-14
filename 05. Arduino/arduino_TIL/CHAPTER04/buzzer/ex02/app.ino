#include <MiniCom.h>
#include <Buzzer.h>

MiniCom com;
Buzzer bz(8);

void check() {
  int value = analogRead(A0);
  int distance = map(value, 0, 1023, 0, 9);
  com.print_i(0, "distance: ", distance);
  if(distance >=5) {
    bz.stop();
    com.print(1, "buzzer off");
  }else {
    bz.setOfftime(500);
    com.print_i(1, "off time", 500);
  }
}

void setup() {
  com.init();
  com.setInterval(100, check);
}

void loop() {
  com.run();
  bz.run();
}