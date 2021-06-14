// 2개 색상은 255로 고정
// 나머지 색상은 0.2초 간격으로 그라데이션
// 0 > 5 > 10 > ... > 255 > 0 > 5 > ...
// 버튼을 누른 경우 그라데이션 효과주는 색상으로 변경
// r > g> b > r > ...

#include <SimpleTimer.h>
#include <ColorLed.h>
#include <Button.h>

ColorLed cled(9,10,11);
Button btn(3);
SimpleTimer timer;

int color = 0;
int value = 0;

void gradation() {
  value = (value + 5) % 255;
  switch(color) {
    case 0:
      cled.rgb(value, 255, 255);
      break;
    case 1:
      cled.rgb(255, value, 255);
      break;
    case 2:
      cled.rgb(255, 255, value);
      break;
  }
}

void changeColor() {
  if(!btn.debounce()) return;
  color = (color + 1) % 3;
  value = 0;
}

void setup() {
  timer.setInterval(200, gradation);
  btn.attachInterrupt(changeColor, FALLING);
}

void loop() {
  timer.run();
}