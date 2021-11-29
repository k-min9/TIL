/**
 * C++ STL 연습하기에 좋은 문제여서 vector로 한 번 풀어보기로 했다.
*/
#include <iostream>
#include <vector>
 
using namespace std;


int main() {

  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);

  // 선언, 입력
  int N;
  cin >> N;
  vector<pair<int, int>> v;

  // 풍선 번호 1부터 N까지
  for(int i=1; i<=N; i++){
    int num;
    cin >> num;

    v.push_back(make_pair(i, num));
  }

  // 빌 때까지 반복
  while(v.empty() != true) {
    
    cout << v.front().first << " ";
    int a = v.front().second;
    v.erase(v.begin());

    // 음수 이동
    if (a<0) {
      for(int j=0; j<abs(a); j++){
        v.insert(v.begin(), v.back());
        v.erase(v.end());
      }
    }
    // 양수 이동
    else {
      for (int j=0; j< a-1; j++) {
        v.push_back(v.front());
        v.erase(v.begin());
      }
    }
  }
  return 0;
}