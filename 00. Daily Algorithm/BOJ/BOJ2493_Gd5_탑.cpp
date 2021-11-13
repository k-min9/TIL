/** 스택 
 * 6 9 7 5 4
 * 스택상황 : 0출력 (1, 6) > 0출력 (2, 9) > 2출력 (2, 9) (3, 5) > 2출력 (2, 9) (4, 7) > 4출력 (2 9) (4 7) (5 4)
 * 
*/

#include <iostream>
#include <stack>
 
using namespace std;
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    
    // 탑 갯수
    int num, height;
    cin >> num;
    stack<pair<int, int>> s;  // 탑번호 인덱스, 높이
    for (int i = 0; i < num; i++) {
        cin >> height;
 
        while (!s.empty()) {
            //수신탑 발견 (높이 비교, 스택 상단이 더 크면 인덱스 출력)
            if (height < s.top().second) {
                cout << s.top().first << " ";
                break;
            }
            //수신탑 찾을 때까지 계속 pop
            s.pop();
        }
        // 스택이 비어있으면 0 출력
        if (s.empty()) {
            cout << 0 << " ";
        }
        //현재 높이를 스택에 푸쉬
        s.push(make_pair(i + 1, height));
    }
     
    return 0;
}  