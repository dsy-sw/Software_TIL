#include <Melody.h>
#include "pitches.h"
#include "pirates.h"

int length = sizeof(notes) / sizeof(int);
Melody md(2, notes, durations, length);

void setup() {
  md.play();
}

void loop() {
  md.run();
}