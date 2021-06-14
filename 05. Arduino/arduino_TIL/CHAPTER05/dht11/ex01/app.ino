#include <DHT.h>
#include <MiniCom.h>
#include <Button.h>

Button btn(3);
DHT dht11(8, DHT11);      // 2초 이상의 시간 간격으로 측정, 더 짧으면 에러 발생
MiniCom com;
bool mode = true;

float g_ff=0.0;
float g_fc=0.0;

void check() {
  float fc = dht11.readTemperature();   // 섭씨 온도 측정
  float ff = dht11.readTemperature(true);   // 화씨 온도 측정
  float fh = dht11.readHumidity();      // 습도 측정

  if(mode) {
  com.print_d(0, "T(C): ",fc);
  } else {
  com.print_d(0, "T(F): ",ff);
  }
  com.print_d(1,"H: ", fh);
}

void onClick() {
  if(!btn.debounce()) return;
  mode = !mode;

  // if(mode) {
  //   com.print_d(0, "T(C): ", g_fc);
  // } else {
  //   com.print_d(0, "T(F): ", g_ff);
  // }
}
void setup() {
  com.init();
  com.setInterval(2000, check);
  dht11.begin();
  btn.attachInterrupt(onClick, FALLING);
}

void loop() {
  com.run();
}