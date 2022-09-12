// 언어 : cpp, deque 구현
// 방법 1. multiset(중복 허용 set)을 이용한 구현
// 방법 2. 큐 두개를 써서 구현, 반대쪽 큐에도 기록하기 위해 map 사용
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>

using namespace std;

priority_queue<int, vector<int>, greater<int>> min_pq;
priority_queue<int, vector<int>, less<int>> max_pq;
map<int, int> dict; // map[x] = 0 이다 : 반대쪽 큐에서 삭제했다.

int T, k, n;
char c;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> T;
	
	while (T) {
	    while (!min_pq.empty()) { min_pq.pop(); }
	    while (!max_pq.empty()) { max_pq.pop(); }
	    dict.clear();
	    
	    cin >> k;
	    
	    for (int i = 0; i < k; i++) {
	        cin >> c >> n;
	        
	        if (c == 'I') {       // 삽입
	            min_pq.push(n);
	            max_pq.push(n);
	            
	            if (dict.count(n) == 0) {
	                dict[n] = 1;
	            }
	            else {
	                dict[n]++;
	            }
	        }
	        else {                  // 삭제
	            if (n == 1) {       // 최대값 삭제
	                while (!max_pq.empty() && dict[max_pq.top()] == 0) {   // 최소값으로 삭제된 수는 스킵
	                    max_pq.pop();
	                }
	                
	                if (!max_pq.empty()) {
	                    dict[max_pq.top()]--;
	                    max_pq.pop();
	                }
	            }
	            else {              // 최소값 삭제
	                while (!min_pq.empty() && dict[min_pq.top()] == 0) {   // 최대값으로 삭제된 수는 스킵
	                    min_pq.pop();
	                }
	                
	                if (!min_pq.empty()) {
	                    dict[min_pq.top()]--;
	                    min_pq.pop();  
	                }
	            }
	        }
	    }
	    
	    while (!max_pq.empty() && dict[max_pq.top()] == 0) {   // 최소값으로 삭제된 수는 스킵
            max_pq.pop();
        }
	    
	    while (!min_pq.empty() && dict[min_pq.top()] == 0) {   // 최대값으로 삭제된 수는 스킵
            min_pq.pop();
        }
	    
	    if (max_pq.empty() || min_pq.empty()) {
	        cout << "EMPTY\n";
	    }
	    else {
	        cout << max_pq.top() << " " << min_pq.top() << "\n";
	    }
	    
	    T--;
	}

	return 0;
}
