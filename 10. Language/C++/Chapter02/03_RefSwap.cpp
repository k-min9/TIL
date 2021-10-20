#include <iostream>
using namespace std;


//C 스타일 포인터 스왑
void SwapByRef(int* ptr1, int* ptr2)
{
	int temp = *ptr1;
	*ptr1 = *ptr2;
	*ptr2 = temp;
}


// 같은 call by reference지만 주소가 아닌 참조자를 이용하는 방법
// 호출 시점에서 초기화 되면서 변수가 들어감
void SwapByRef2(int &ref1, int& ref2)
{
	int temp=ref1;
	ref1=ref2;
	ref2=temp;
}

int main(void)
{
	int val1=10;
	int val2=20;

	SwapByRef(&val1, &val2);

	cout<<"val1: "<<val1<<endl;
	cout<<"val2: "<<val2<<endl;

	SwapByRef2(val1, val2);

	cout<<"val1: "<<val1<<endl;
	cout<<"val2: "<<val2<<endl;
	return 0;
}