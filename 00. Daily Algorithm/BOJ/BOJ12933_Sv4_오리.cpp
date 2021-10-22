/**
 * 언어 : cpp, 풀이 보면 알겠지만 시간복잡도가 전혀 고려되지 않았다.
*/
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {

	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	string input; 
  cin >> input;

	int len = input.length();
	vector<int> arr;
	vector<int> num(6, 0);
	for (int i = 0; i < len; i++) {
		if (input[i] == 'q') {
			arr.push_back(1);
			num[1]++;
		}
		else if (input[i] == 'u') {
			arr.push_back(2);
			num[2]++;
		}
		else if (input[i] == 'a') {
			arr.push_back(3);
			num[3]++;
		}
		else if (input[i] == 'c') {
			arr.push_back(4);
			num[4]++;
		}
		else if (input[i] == 'k') {
			arr.push_back(5);
			num[5]++;
		}
	}
	if (num[1] != num[2] || num[1] != num[3] || num[1] != num[4] || num[1] != num[5]) {
		cout << -1;
		return 0;
	}

	vector<vector<int>> duck;
	vector<int> cnt;
	for (int i = 0; i < len; i++) {
		int now = arr[i];
		bool flag = false;
		if (now == 1) {
			for (int k = 0; k < duck.size(); k++) {
				if (duck[k].empty()) {
					duck[k].push_back(1);
					flag = true;
					break;
				}
			}
			if (flag) continue;
			vector<int>s;
			s.push_back(1);
			duck.push_back(s);
			cnt.push_back(0);
			continue;
		}
		bool err = true;
		for (int j = 0; j < duck.size(); j++) {
			if (duck[j].empty()) continue;
			if (duck[j].back() == now - 1) {
				duck[j].push_back(now);
				err = false;
				if (duck[j].size() == 5) {
					duck[j].clear();
					cnt[j]++;
				}
				break;
			}
		}
		if (err) {
			cout << -1;
			return 0;
		}
	}
	int res = 0;
	for (int i = 0; i < cnt.size(); i++) {
		if (cnt[i] > 0)
			res++;
	}
	if (res == 0)
		cout << -1;
	else
		cout << res;
	return 0;
}