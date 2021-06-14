const int buzzer_pin = 2;

void setup() {
  pinMode(buzzer_pin, OUTPUT);
}

void loop() {
  digitalWrite(buzzer_pin, HIGH);
  delay(1000);
  digitalWrite(buzzer_pin, LOW);
  delay(1000);
}