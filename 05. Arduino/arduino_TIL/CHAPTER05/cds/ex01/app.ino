#include <MiniCom.h>
#include <Led.h>

MiniCom com;
Led led(8);

void check() {
  int ad_cds = analogRead(A0);
  float v_cds = (ad_cds/1024.)*5;

  com.print_i(0, "AD_CDS : " , ad_cds);
  com.print_d(1, "V_CDS : ", v_cds);

  if(ad_cds<700) {
    led.on();
  } else {
    led.off();
  }
}

void setup() {
  com.init();
  com.setInterval(1000, check);
}

void loop() {
  com.run();
}