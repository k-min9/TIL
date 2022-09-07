// 언어 : cpp, 중위 순회와 유사한 순회를 해서 순회 이해를 하나 보자.
#include<iostream>
#include<vector>
#include<algorithm>
#include<map>

using namespace std;

// 전체 이동횟수, 오른쪽 자식 노드로 이동 수
int n, a=-1, r=-1;

map<int,pair<int,int>> relation;

void input(){
    ios_base::sync_with_stdio(false);
    cin.tie(0),cout.tie(0);
    cin >> n;
    for(int i=0,a,b,c; i<n; i++){
        cin >> a >> b >> c;
        relation[a].first = b;
        relation[a].second = c;
    }
}

// flag : is왼쪽노드탐색중 >> r 쌓기
void travel(int cur, bool flag){
    if(cur == -1) return;

    a ++, travel(relation[cur].first,0);

    if(flag) r++, travel(relation[cur].second,1);
    else travel(relation[cur].second,0);

}
void solution(){

    input();
    travel(1,1);
    cout << 2* a - r;
}

int main(){
    solution();
    return 0;
}
