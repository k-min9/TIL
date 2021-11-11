/** 플로이드 와샬 in cpp */
#include <iostream>
#include <algorithm>
#include <vector>

// 상수
#define INF 987654321

using namespace std;
int dist[51][51];
int num,a,b;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    // 세팅
    cin >> num;
    for(int i=1;i<=num;i++)
        for(int j=1;j<=num;j++){
            if(i==j) continue;
            else dist[i][j] = INF;
        }

    // 입력
    while(true){
        cin >> a >> b;
        if(a == -1) break;
        dist[a][b]=1;
        dist[b][a]=1;
    }

    // floid
    for(int t=1;t<=num;t++)
        for(int i=1;i<=num;i++)
            for(int j=1;j<=num;j++)
                dist[i][j] = min(dist[i][j], dist[i][t] + dist[t][j]);

    int answer = 1000;
    vector<int> answers;
    for(int i=1 ; i<=num ; i++){
        int temp = 0;
        for(int j=1 ; j<=num ; j++)
            temp = max(temp, dist[i][j]);
        if(temp < answer){
            answers.clear();
            answer = temp;
            answers.push_back(i);
        }
        else if(temp==answer)
            answers.push_back(i);
    }

    // 회장 후보, 점수, 후보 오름차순 출력
    sort(answers.begin(),answers.end());
    cout << answer << " "<<answers.size()<<'\n';
    for(int i=0;i<answers.size();i++)
        cout << answers[i]<<" ";
    return 0;
}