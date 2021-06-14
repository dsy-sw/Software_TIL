#include <Led.h>
#include <SimpleTimer.h>
#include <Button.h>

SimpleTimer timer;

Led led1(9);
Led led2(10);
Led led3(11);
Led led4(12);
int timer1Id;

Button btn(3);

void blink1() {
  led1.toggle();
}
void blink2() {
  led2.toggle();
}
void blink4() {
  led3.toggle();
}
void blink4() {
  led4.toggle();
}

void onClick() {
  if(!btn.debounce()) return;
  timer.toggle(timer1Id);
}
void setup() {
  timer1Id = timer.setInterval(200, blink1);
  timer.setInterval(400,[](){ led2.toggle();});
  timer.setInterval(400,[](){ led3.toggle();});
  timer.setInterval(400,[](){ led4.toggle();});

  // btn.attachInterrupt(onClick, FALLING);
  // btn.attachInterrupt([](){
  //   if(!btn.debounce()) return;
  //   timer.toggle(timer1Id);
  // }, FALLING);
  btn.setCallback([]()){timer.toggle(timer1Id)};
}

void loop() {
  timer.run();
  btn.check();    //polling
}