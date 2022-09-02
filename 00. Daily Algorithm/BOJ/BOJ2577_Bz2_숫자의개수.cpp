// 언어 : cpp, 숫자 -> 문자 카운트

#include <iostream>
#include <string>
using namespace std;
 
int main(int argc, const char *argv[]) {
 
	int count[10] = {}; // 0으로 초기화를 해야한다. ({}, {0,}, {0})
	int a, b, c;
 
	cin >> a >> b >> c;
 
	int res = a * b * c;  // 오버플로우 걱정 없음
	string s = to_string(res);  // 숫자 -> 문자
 
  // for each + 아스키 코드 
	for (char ch : s) {
		count[ch - '0']++;
	}
 
	// 출력
	for (int v : count) {
		cout << v << "\n";
	}
	return 0;
}