// 기준 거리로 진입하면 문을 열어줌
// 기준 거리를 벗어나면 문을 닫음
// 문 열고 닫기는 led on/off로 대체
// 진입한 경우 벗어날 때까지 거리 변화를 LDC에 출력
// 필요하다면 Ultra 소스 수정

#include <MiniCom.h>
#include <Ultra.h>
#include <Led.h>

Ultra ultra(8, 9);
MiniCom com;
Led led(7);

void open_door() {
  led.on();
  com.print(1, "Door opend");

}

void close_door() {
  led.off();
  com.print(0, "Dist.(cm): ");
  com.print(1, "Door closed");
}

void check() {
  int distance = ultra.run();
  if(distance) {
    com.print_i(0, "Dist.(cm): ", distance);
  }
}  

void setup() {
  com.init();
  ultra.setThreshold(15, open_door, close_door);
  com.setInterval(50, check);
  com.print(0, "Dist.(cm): -");
  com.print(1, "Door closed");

}

void loop() {
  com.run();
}