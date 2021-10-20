#include <iostream>
using namespace std;

void MyFunc(void)
{
  cout<<"func 1 called"<<endl;
}

void MyFunc(char c)
{
  cout<<"func 2 called"<<endl;
}

void MyFunc(int a, int b)
{
  cout<<"func 3 called"<<endl;
}

int main(void)
{
  MyFunc();
  MyFunc(2, 3);
  MyFunc('2');
}