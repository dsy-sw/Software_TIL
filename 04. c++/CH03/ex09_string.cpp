#include <iostream>
#include <string>

using namespace std;
int main(int argc, char const  *argv[]){
  string s = "When in Rome, do as the Romans.";

  for(auto& ch: s){
    cout << ch << ' ';
  }
  return 0;
}