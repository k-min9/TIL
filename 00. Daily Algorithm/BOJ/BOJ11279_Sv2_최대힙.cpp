// 언어 : cpp, 자료구조 최대 힙 만들기
// 자연수로 추가, 0으로 가장 큰 값 출력 후 제거

#include <iostream>
#include <queue>
#include <vector>
using namespace std;
 
int main(){

    ios::sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    vector<int> result;
    int n, x;
    cin >> n;
 
    priority_queue<int> q;  // int형 우선순위 큐

    for (int i = 0; i < n; i++){
        cin >> x;
        if(x != 0){
            q.push(x);
        } else {
            // 비어있으면 0
            if(q.empty()){
                result.push_back(0);
            } else {
                // 가장 윗 값 출력
                result.push_back(q.top());
                q.pop();
            }
        }
    }
    for (int i = 0; i < result.size(); i++){
        cout << result[i] << '\n';
    }
        return 0;
}


