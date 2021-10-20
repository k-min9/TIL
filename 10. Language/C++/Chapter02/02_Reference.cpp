#include <iostream>
using namespace std;

int main(void)
{
	int num1 = 1020;
	// 참조자, 별명, 주소의 위치 등으로 생각하면 편하다. 변수에 대해서만 가능(선언과 동시에 참조해야 함)
	int &num2 = num1;  

	num2=3047;
	cout<<"VAL: "<<num1<<endl;
	cout<<"REF: "<<num2<<endl;

	num1+=1;
	cout<<"VAL: "<<num1<<endl;
	cout<<"REF: "<<num2<<endl;

	num2+=1;
	cout<<"VAL: "<<num1<<endl;
	cout<<"REF: "<<num2<<endl;

	cout<<"VAL: "<<&num1<<endl;
	cout<<"REF: "<<&num2<<endl;
	return 0;
}