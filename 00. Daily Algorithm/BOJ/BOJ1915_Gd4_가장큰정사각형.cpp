#include <vector>
#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int arr[1001][1001];

int main(){
   
    int n, m;
    cin>>n>>m;

    // 입력
    for(int i = 1; i <=n;i++){
        string s;
        cin>>s;
        for(int j = 0 ;j < m ; j++){
            arr[i][j+1] = s[j] - 48; //'0'
        }
    }

    // 풀기
    int ans = 0;  // 정답 정사각형 한 변의 길이
    for(int i = 1 ; i <= n; i ++){
        for(int j = 1 ; j <= m; j++){
            
            if(arr[i][j] != 0){
                arr[i][j] = min(min(arr[i-1][j], arr[i][j-1]),arr[i-1][j-1]) + 1;
                ans = max(arr[i][j],ans);
            }
        }
    }

    cout<<ans*ans<<endl;

    return 0;
}