/**누가 봐도 스택. 
 * A타입 괄호와 B타입 괄호가 제대로 닫히는지 확인하는게 이번 목표*/

#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main(void) {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  int N;
  cin >> N;
  int answer = 0;
  for (int i = 0; i < N; i++) {
    string str;
    cin >> str;
    stack<char> chk;

    for (int j = 0; j < str.length(); j++) {
      //스택 최상단과 다음 스트링 비교
      if (!chk.empty() && chk.top() == str[j])
        chk.pop();
      else
        chk.push(str[j]);
    }

    if (chk.empty()) answer++;
  }

  cout << answer << "\n";
  return 0;
}
