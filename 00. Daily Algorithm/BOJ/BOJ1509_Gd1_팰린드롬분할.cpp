/**
 * pld[i][j] : i 부터 j 까지가 팰린드롬인지 기록
 * dp[i] = min(dp[i], dp[j-1]+1)
*/

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string s;
int pld[2501][2501];
int d[2501];

int main() {
	cin >> s;
	s.insert(0, " ");
	int N = s.length();

  // 총길이 1, 2
	for (int i = 1; i <= N; i++) pld[i][i] = 1; //1
	for (int i = 1; i < N; i++) if (s[i] == s[i + 1]) pld[i][i + 1] = 1; //2

	//3이상
	for (int i = 2; i < N; i++)
		for (int j = 1; j <= N - i; j++)
			if (s[j] == s[i + j] && pld[j + 1][j + i - 1]) pld[j][j + i] = 1;

	for (int i = 1; i < N; i++){
		d[i] = 2147483647;
		for (int j = 1; j <= i; j++){
			if (pld[j][i]) d[i] = min(d[i], d[j - 1] + 1);
		}
	}
	cout << d[N-1] << endl;
	return 0;
}