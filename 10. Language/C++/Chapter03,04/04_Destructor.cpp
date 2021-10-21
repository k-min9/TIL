#include <iostream>
#include <cstring>
using namespace std;

class Person
{
private:
	char * name;
	int age;
public:
	Person(const char * myname, int myage)
	{
		int len=strlen(myname)+1;
		name=new char[len];
		strcpy(name, myname);
		age=myage;
	}

	void ShowPersonInfo() const
	{
		cout<<"name: "<<name<<endl;
		cout<<"age: "<<age<<endl;
	}
	
	// ~ 붙은게 소멸자, 클래스가 소멸할때 호출된다. 그 외는 생성자와 동일하다.
	~Person()
	{
		delete []name;
		cout<<"called destructor!"<<endl;
	}
};

int main(void)
{
	Person man1("Lee dong woo", 29);
	Person man2("Jang dong gun", 41);
	man1.ShowPersonInfo();
	man2.ShowPersonInfo();
	return 0;
}