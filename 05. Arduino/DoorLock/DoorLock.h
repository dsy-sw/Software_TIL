#pragma once
#include <Arduino.h>
#include <EEPROM.h>
#include<Led.h>
#include <Servo.h>


class DoorLock {
protected:
  String password;
  Led led;
  Servo door;
  String password;
public:
  DoorLock(int led_pin=4);
  String read_password();
  void init();
  void write_password(String password);
  void beep(int interval = 100);
  void open_door();
  void reset();
};