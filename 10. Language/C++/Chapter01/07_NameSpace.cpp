#include <iostream>
using namespace std;

namespace Parent{
  int num = 2;
  namespace SubOne{
    int num = 3;
  }
  namespace SubTwo{
    int num = 4;
  }
}


int main(void)
{
  cout << Parent::num << endl;
  cout << Parent::SubOne::num << endl;
  cout << Parent::SubTwo::num << endl;

  // namespace 별명 짓기
  namespace Two = Parent::SubTwo;
  cout << Two::num << endl;
}