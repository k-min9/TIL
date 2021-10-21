#include <iostream>
#include <cstring>
using namespace std;

namespace CAR_CONST
{
	enum
	{
		ID_LEN		=20,
		MAX_SPD		=200,
		FUEL_STEP	=2,
		ACC_STEP	=10,
		BRK_STEP	=10
	};
}

class Car
{
	// 필드를 private에 둬서 접근 막고
private:
	char gamerID[CAR_CONST::ID_LEN];	
	int fuelGauge;		
	int curSpeed;		
	// 함수를 public에 둬서 제어, 함수 내용은 밖에 분리
public:
	void InitMembers(char * ID, int fuel);  // 필드 접근
	void ShowCarState();  // 현재 상태
	void Accel();  // 가속
	void Break();  // 감속
};

void Car::InitMembers(char * ID, int fuel)
{
	strcpy(gamerID, ID);
	fuelGauge=fuel;
	curSpeed=0;
};
void Car::ShowCarState()
{
	cout<<"User ID : "<<gamerID<<endl;
	cout<<"Fuel : "<<fuelGauge<<"%"<<endl;
	cout<<"Current Speed : "<<curSpeed<<"km/s"<<endl<<endl;
}
void Car::Accel()
{
	if(fuelGauge<=0)
		return;
	else
		fuelGauge-=CAR_CONST::FUEL_STEP;

	if((curSpeed+CAR_CONST::ACC_STEP)>=CAR_CONST::MAX_SPD)
	{
		curSpeed=CAR_CONST::MAX_SPD;
		return;
	}
	curSpeed+=CAR_CONST::ACC_STEP;
}
void Car::Break()
{
	if(curSpeed<CAR_CONST::BRK_STEP)
	{
		curSpeed=0;
		return;
	}
	curSpeed-=CAR_CONST::BRK_STEP;
}

int main(void)
{
	Car run99;
	run99.InitMembers("run99", 100);
	run99.Accel();
	run99.Accel();
	run99.Accel();
	run99.ShowCarState();
	run99.Break();
	run99.ShowCarState();
	return 0;
}