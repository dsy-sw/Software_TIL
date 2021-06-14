#pragma once
#include "Car.hpp"

class Taxi: public Car {
protected:
  int fee;
public:
  void setFee(int f);
  int getFee();
};