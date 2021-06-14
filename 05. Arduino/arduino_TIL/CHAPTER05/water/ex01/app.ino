#include <MiniCom.h>
#include <Buzzer.h>

MiniCom com;
int buzzer = 8;

void check() {
  int d_value = analogRead(A0);
  int a_value = d_value * 5. / 1024.;
  com.print_i(0, "D: ", d_value);
  com.print_i(1, "A: ", a_value);

  if(d_value > 506) {
    digitalWrite(buzzer, HIGH);
  } else {
    digitalWrite(buzzer, LOW);
  }
}

void setup() {
  com.init();
  com.setInterval(1000, check);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  com.run();
}