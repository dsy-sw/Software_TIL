#include <iostream>
using namespace std;

class Shape{
  protected:
  int x,y;
  public:
  void draw() {}
  void move() {}
};

class Reactangle: public Shape{
  protected:
  int width, height;
  public:
  int calcArea(){
    return width*height;
  }
};

int main(){
  Reactangle r;
  r.x = 10;
  r.width = 200;

  r.calcArea();
  r.move();
  return 0;
}