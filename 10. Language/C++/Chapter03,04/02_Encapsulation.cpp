#include <iostream>
using namespace std;

/**
 * 캡슐화 : 하나의 목적(종합 감기) 하에 둘 이상의 목적이 모여서 목적을 달성, >> 그래서 범위 정하기가 힘듬
*/

class SinivelCap    // 콧물
{
public: 
	void Take() const {cout<<"action 1"<<endl;}
};

class SneezeCap    // 재채기
{
public: 
	void Take() const {cout<<"action 2"<<endl;}
};

class SnuffleCap   // 코막힘
{
public: 
	void Take() const {cout<<"action 3"<<endl;}
};

class CONTAC600 
{
private:
	SinivelCap sin;
	SneezeCap sne;
	SnuffleCap snu;

public:
	// const 함수로, 멤버변수 변하지 않음을 보장
	void Take() const
	{
		//순서가 중요
		sin.Take();
		sne.Take();
		snu.Take();
	}
};

class ColdPatient
{
public:
	void TakeCONTAC600(const CONTAC600 &cap) const { cap.Take(); }
};

int main(void)
{
	CONTAC600 cap;
	ColdPatient sufferer;
	sufferer.TakeCONTAC600(cap);
	return 0;
}