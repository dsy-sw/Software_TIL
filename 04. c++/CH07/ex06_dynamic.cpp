#include <iostream>
#include <string>
using namespace std;

class Dog{
  public:
  int age;
  string name;

  Dog(){
    cout << "Dog init call" << endl;
    age = 1;
    name = "baduk";
  }
  ~Dog(){
    cout << "Dog destroytor call" << endl;
  }
  };

  int main(){
    Dog *pDog = new Dog;
    delete pDog;
    return 0;
  }