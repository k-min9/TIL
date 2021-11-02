/** 이 문제는 기교쓰지 말고 그리디하게 푸는게 제일 빠르고 정확하다.*/
#include <iostream>

using namespace std;

int main(void) {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  int N, M;
  cin >> N >> M;
  int answer = 1;
  while (N < M) {
    if (M % 10 == 1) {
      M /= 10;
      answer += 1;
    }
    else if (M %2 == 0) {
      M /= 2;
      answer += 1;
    }
    else {
      cout << -1;
      exit(0);
    }
  }

  if (N == M) cout << answer;
  else cout << -1;

  return 0;
}