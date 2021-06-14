// 0.2초 간격으로 타이머 사용해서
// 랜덤하게 생상 변경

#include <ColorLed.h>
#include <SimpleTimer.h>

ColorLed cled(9, 10, 11);
SimpleTimer timer;

void setup() {
  timer.setInterval(200,[](){
    cled.random();
  });
}

void loop() {
  timer.run();
}