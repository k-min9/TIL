#include <iostream>
using namespace std;

// static : C와 성질 동일, C++에서는 모든 객체가 공유하는 구조(변수, 함수)/클래스 변수 정도로 쓸 수 있음

class SoSimple
{
private:
	static int simObjCnt;
public:
	SoSimple()
	{
		simObjCnt++;
		cout<<"SoSimple Objenct No."<<simObjCnt<<endl;
	}
};
int SoSimple::simObjCnt=0; // static은 꼭 이렇게 초기화 해줘야 함 >> const static일 경우 위에 직접 정의

class SoComplex
{
private:
	static int cmxObjCnt;
	
public:
	SoComplex()
	{
		cmxObjCnt++;
		cout<<"SoComplex Objenct No."<<cmxObjCnt<<endl;
	}
	SoComplex(SoComplex &copy)
	{
		cmxObjCnt++;
		cout<<"SoComplex Objenct No."<<cmxObjCnt<<endl;
	}
};
int SoComplex::cmxObjCnt=0;

int main(void)
{
	SoSimple sim1;
	SoSimple sim2;

	SoComplex cmx1;
	SoComplex cmx2=cmx1;
	SoComplex();
	return 0;
}