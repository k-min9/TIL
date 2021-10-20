#include <iostream>
using namespace std;

void MyFunc(int a, int b = 3) // 기본값이 있다 = 우측으로 보내라
{
  cout<<a<<b<<endl;
}

int main(void)
{
  MyFunc(2, 1);
  MyFunc(2);
}