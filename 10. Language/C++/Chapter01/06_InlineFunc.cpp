#include <iostream>
using namespace std;
#define SQUARE2(x) ((x)*(x))


// 매크로 함수 처럼 전처리는 해주면서 여러 기능 부여가 가능해지지만, 자료형에 의존적임
inline int SQUARE(int x)
{
  return x*x;
}

int main(void)
{
  cout<<SQUARE(5)<<endl;
  cout<<SQUARE2(1.4);
}