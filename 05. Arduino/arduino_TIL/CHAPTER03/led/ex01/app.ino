// LED 풀업/풀다운 연결핀 HIGH 출력 확인
const int pd_led_pin = 11;   // 풀다운 연결핀
const int pu_led_pin = 10;   // 풀업 연결핀


void setup() {
pinMode(pd_led_pin, OUTPUT);    // 풀다운 LED 연결핀 출력 설정
pinMode(pu_led_pin, OUTPUT);    // 풀업 LED 연결핀 출력 설정
}

void loop() {
digitalWrite(pd_led_pin, HIGH);   // 풀다운 LED 연결핀 HIGH 출력
digitalWrite(pu_led_pin, HIGH);   // 풀업 LED 연결핀 HIGH 출력
delay(1000);

digitalWrite(pd_led_pin, LOW);   // 풀다운 LED 연결핀 HIGH 출력
digitalWrite(pu_led_pin, LOW);   // 풀업 LED 연결핀 HIGH 출력
delay(1000);
}