#include <iostream>
#include <string.h>
using namespace std;


// malloc->new , 형변환이 필요 없고, 바이트 단위가 아니어서 알기 쉬움
// 실제로는 new와 malloc 사이에 동작 차이가 있고, C++내에서 malloc은 사용해서 안된다.
char* MakeStrAdr(int len)
{
	// char * str=(char*)malloc(sizeof(char)*len);
	char* str = new char[len];
	return str;
}

int main(void)
{
	char* str=MakeStrAdr(20);
	strcpy(str, "I am so happy~");
	cout<<str<<endl;
	// free(str); free->delete
	delete []str;  // 배열의 소멸
	return 0;
}