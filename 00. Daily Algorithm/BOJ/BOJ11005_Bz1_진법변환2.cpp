// 언어 : cpp, 기업 채용 기출 유사 문제
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
  int n, b;
  cin >> n >> b;

  string answer;
  while (n!=0) {
    int temp = n % b;
    n /= b;
    if (temp > 9) {
      temp = temp - 10 + 'A';  // 아스키코드
      answer += temp;
    } else {
      answer += ('0'+temp);
    }
  }

  reverse(answer.begin(), answer.end());

  cout << answer << "\n";

  return 0;

}
