#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;
// 하위버전 호환성을 위해 C언어 헤더 사용 가능. .h를 빼고 앞에 c를 붙이면 됨


int main(void)
{
	char str1[]="Result";
	char str2[30];

	strcpy(str2, str1);
	printf("%s: %f \n", str1, sin(0.14));
	printf("%s: %f \n", str2, abs(-1.25));
	return 0;
}