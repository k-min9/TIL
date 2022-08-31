// 언어 : cpp, 
// (100~1~|01)~ 를 만족하는지 = 0으로 시작시 01인지 1로 시작시 100~1~인지 체크를 끝까지 반복
// 100~1~ = 00 확인후 0을 죄다 건너뛰고 나오는 1이 있는지 체크

#include<iostream>
#include<string>

using namespace std;

bool isSubmarine(string N) {
	int i = 0;
  int s = N.length();
	while (i < s) {
		if (N[i] == '0') {
			if (i + 1 >= s) return false;
			if (N[i + 1] != '1') return false;
			i += 2;
		}
		else { // 시작이 1이면 최소 1 00 1
			if (i + 3 >= s) return false;
			if (!(N[i + 1] == '0' && N[i + 2] == '0')) return false; // 일단 무조건 뒤에 0이 2개 나와야됨.
			i++;
			while (i < s && N[i] == '0')
				i++;
			if (i >= s) return false; // 1 뒤에붙은 0들을 다 추적했더니 끝나버린 경우.
			i++;
			while (i < s && N[i] == '1') {
				if (i + 2 < s && N[i + 1] == '0' && N[i + 2] == '0') break;
				i++;
			}
		}
	}
	return true;
}

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	string s;
	cin >> s;
	if (isSubmarine(s)) cout << "SUBMARINE";
	else cout << "NOISE";
	return 0;
}