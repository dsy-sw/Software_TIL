#include <Led.h>
#include <Buzzer.h>
#include <MiniCom.h>

Ultra ultra(8,9);
Buzzer bz(10);
MiniCom com;

int interval[] {
  100,200,400,700,1000
};

void bz_off(){
  com.print(0, "Dist.(cm): -");
  com.print(0, "interval: -");
  bz.stop();
}

void check() {
  int distance = ultra.run();
  if(distance) {
    int ix = map(distance, 1, 15, 0, 4);
    bz.setOfftime(interval[ix]);
    com.print_i(0, "Dist.(cm): ", distance);
    com.print_i(0, "interval: ", interval[ix]);
  }
}

void setup(){
  com.init();
  ultra.setThreshold(15, NULL, bz_off);
  com.setInterval(50, check);
  com.print(0, "Dist.(cm): -")
}

void loop() {
  com.run();
  bz.run();
}