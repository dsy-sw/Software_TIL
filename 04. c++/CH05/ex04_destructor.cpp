#include <string.h>
#include <iostream>
using namespace std;

class Mystring{
  private:
  char *s;
  int size;

  public:
  Mystring(char *c){
    size = strlen(c) + 1; // null
    s = new char[size];
    strcpy(s, c);
  }

  ~Mystring(){
    cout << "destructor called!";
    delete[]s;
  }
};

int main(){
  Mystring str("abcdefghijklmn");
}