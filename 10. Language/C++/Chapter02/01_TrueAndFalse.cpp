#include <iostream>
using namespace std;

int main(void)
{
	int num=10;
	int i=0;

	cout<<"true: "<<true<<endl;  // TRUE = 1
	cout<<"false: "<<false<<endl;  // FALSE = 0

	while(true)
	{
		cout<<i++<<' ';
		if(i>num)
			break;
	}
	cout<<endl;

	// 숫자의 사이즈 = 4 / Boolean의 사이즈 = 1, 단지 0, 1로변환이 될 뿐
	cout<<"sizeof 1: "<<sizeof(1)<<endl;
	cout<<"sizeof 0: "<<sizeof(0)<<endl;
	cout<<"sizeof true: "<<sizeof(true)<<endl;
	cout<<"sizeof false: "<<sizeof(false)<<endl;
	return 0;
}