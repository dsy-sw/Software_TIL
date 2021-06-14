#include <iostream>
using namespace std;

int test(int arr[]){
  int s = sizeof(arr);
  cout << "array size : " << s << endl;
  arr[0] = 10;
  return arr[0];
}

int main(int argc, char const *argv[]){
  int n[] = {1, 2, 3, 4, 5};
  cout << "array n size : " << sizeof(n) << endl;
  int m = test(n);

  cout << "result : " << n[0] << endl;
  return 0;
}