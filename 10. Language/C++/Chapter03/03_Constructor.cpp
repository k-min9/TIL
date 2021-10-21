#include <iostream>
using namespace std;

class SimpleClass
{
	int num1;
	int num2;

public:
/**
 * 생성자 : 클래스와 이름 동일, 초기화 담당
 * 반환형이 정해져있지 않고, 반환하지 않으며, 오버로딩 가능하다.
*/
	SimpleClass()
	{
		num1=0;
		num2=0;
	}
	SimpleClass(int n) // 오버로딩 가능, 마찬가지로 default값 넣을때 두 개 이상의 함수가 호출되지 않게 주의
	{
		num1=n;
		num2=0; 
	}
	SimpleClass(int n1, int n2) : num1(n1), num2(n2)  // 멤버 이니셜라이저 : 성능상 이득 + 훨씬 명시적
	{
		// num1=n1;
		// num2=n2;
	}

	/* 객체 생성 함수는 밖으로 빼면 컴파일러가 헷갈려서 오류하니까 밖으로 빼면 안된다!
	SimpleClass(int n1=0, int n2=0)
	{
		num1=n1;
		num2=n2;
	}
	*/

	void ShowData() const
	{
		cout<<num1<<' '<<num2<<endl;
	}
};

int main(void)
{
	SimpleClass sc1;
	sc1.ShowData();

	SimpleClass sc2(100);
	sc2.ShowData();

	SimpleClass sc3(100, 200);
	sc3.ShowData();
	return 0;
}