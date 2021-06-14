#include <iostream>
using namespace std;

int main(){
  int number = 0;
  int *p = &number;

  cout << p << endl;
  cout << *p << endl;

  return 0;
}