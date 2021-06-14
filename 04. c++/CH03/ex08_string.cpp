#include <iostream>
using namespace std;

int main(int argc, char const *argv[]){
  string s = "When in Rome, do as the Romans.";

  int size = s.size();
  int index = s.find("Rome");

  cout << size << endl;
  cout << index << endl;

  return 0;
}