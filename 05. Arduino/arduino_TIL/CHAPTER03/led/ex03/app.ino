int leds[4] {4, 5, 6, 7};
int current = 0;

void setup() {
  for(auto &i :leds) {
    pinMode(i, OUTPUT);
  }
}

void loop() {
  for(int i=0; i<4; i++) {
    int value = i == current;
    digitalWrite(leds[i], value);   // 1: true -> HIGH, 0: false -> LOW
  }
  delay(100);
  current = (current+1)%4;    // 나머지 연산자: 0, 1, ,2, 3만 가지도록
}