#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
  bool b;
  b = (1 == 2);

  cout << std::boolalpha;
  
  cout << b << endl;

  return 0;
}