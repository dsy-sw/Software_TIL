#pragma once
#include <string>
using namespace std;

class Car {
    protected:
    int speed;      // 속도
    int gear;       // 기어
    string color;   // 색상
public:
    int getSpeed();
    void setSpeed(int s);
};