#include <iostream>
using namespace std;

// 참조형을 반환 (참조형 반환 함수는 항상 지역변수를 반환하지 않게 주의하자!)
int& RefRetFuncOne(int &ref)
{
	ref++;
	return ref;
}

int main(void)
{
	int num1=1;
	int num2=RefRetFuncOne(num1); // 참조형이 int로 변환되어 값이 저장

	num1+=1;
	num2+=100;
	cout<<"num1: "<<num1<<endl;
	cout<<"num2: "<<num2<<endl;
	return 0;
}