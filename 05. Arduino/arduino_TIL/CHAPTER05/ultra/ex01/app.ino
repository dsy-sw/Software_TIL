#include <MiniCom.h>


int echoPin = 8;
int triggerPin = 9;

MiniCom com;

void check() {
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);

  int distance = pulseIn(echoPin, HIGH) / 58;
  com.print_i(0, "Dist.(cm): ", distance);
}

void setup() {
  com.init();
  com.setInterval(1000, check);
  // Serial.begin(9600);
  pinMode(echoPin, INPUT);
  pinMode(triggerPin, OUTPUT);
}

void loop() {
  com.run();
}