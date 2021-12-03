/**
 * 투 포인터로 전진하면서 풀면 될 것 같은데
 * 
*/
#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int N,M;
	cin >> N >> M;
	
	vector<int> temp;

	for(int i=0 ; i<N ; i++){
		int a;
		cin >> a;
		temp.push_back(a);
	}

  // 투 포인터	
	int left = 0, right = 0;
	int cnt = 0;
	int sum = 0;
	while(right <= N){
		if(sum < M){
			sum += temp[right++];
		}
		else if(sum > M){
			sum -= temp[left++];
		}
		else{
			cnt++;
			sum += temp[right++];
		}
	}
	cout << cnt;
	return 0;
}


