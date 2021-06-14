// 버튼을 누르면
// LED가 blink 되고
// 한번 더 눌렀을 때 led 꺼짐

#include <Button.h>
#include <Led.h>
#include <MiniCom.h>

MiniCom com;
Button btn(D5);
Led led(D6);

bool state = false; // true: blink모드, false: off모드
int timer_id = -1;

void check() {
  if(!state) {
    int timer_id = com.setInterval(500, [](){
      com.print(0, "Blink mode");
      led.toggle();
    });
    state = true;
  } else {
    led.off();
    state = false;
    com.print(0, "Off mode");
    SimpleTimer& timer = com.getTimer();
    timer.deleteTimer(timer_id);
  }
}

void setup()
{
	com.init();
  btn.setCallback(check);
  com.print(0, "Off mode");
}

void loop()
{
  btn.check();
	com.run();
}
