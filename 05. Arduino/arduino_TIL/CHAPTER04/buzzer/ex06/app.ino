#include "pitches.h"
#include "pirates.h"
#include <MiniCom.h>
#include <Melody.h>
#include <Button.h>
#include <Led.h>


MiniCom com;

int length = sizeof(notes) / sizeof(int);
Melody md(2, notes, durations, length);

Button btn(3);
Led leds[] {
  Led(8), Led(9), Led(10), Led(11)
};

void onClick(){
  if(!btn.debounce()) return;
  int state = md.toggle(true);    // true면 pause

}

void turnLed(int count) {
  for(int i=0; i<4; i++) {
    if(count == 0) {
      leds[i].off();
      continue;
    }

    if(count < i) {
      leds[i].on();
    }else {
      leds[i].off();
    }
  }
}

void led_level() {
  int note = md.getNote();
  int count = 0;

  if(note != 0) {
    count = map(note, 220, 440, 1, 4);
  }
  turnLed(count);
}

void setup() {
  com.init();
  com.setInterval(100, led_level);
  btn.attachInterrupt(onClick, FALLING);
}

void loop() {
  com.run();
  md.run();
}