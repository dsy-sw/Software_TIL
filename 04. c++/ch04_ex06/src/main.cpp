#include <iostream>
#include "Car.hpp"
using namespace std;

int main() {
    Car myCar;

    myCar.setSpeed(100);

    cout <<"speed : " << myCar.getSpeed() <<endl;

    return 0;
}