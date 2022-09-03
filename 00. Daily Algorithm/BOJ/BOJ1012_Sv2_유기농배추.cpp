// 언어 : cpp, DFS

#include <iostream>
using namespace std;
 
const int MAX = 51;
int T, M, N, K;
int map[MAX][MAX];
int visited[MAX][MAX];
int dy[] = {0,0,-1,1};
int dx[] = {-1,1,0,0};
 
void reset() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            map[i][j] = 0;
        }
    }
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            visited[i][j] = 0;
        }
    }
}
 
void DFS(int y, int x) {
    visited[y][x] = 1;
 
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
 
        if (nx < 0 || nx >= M || ny < 0 || ny >= N)
            continue;
        
        if (map[ny][nx] == 1 && visited[ny][nx] == 0) {
            DFS(ny, nx);
        }
    }
}
 
int main() {
    cin >> T;
 
    while (T--) {
        cin >> M >> N >> K;
 
        reset();
 
        while (K--) {
            int x, y;
            cin >> x >> y;
            map[y][x] = 1;
        }
 
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 1 && visited[i][j] == 0) {
                    DFS(i, j);
                    cnt++;
                }
            }
        }
 
        cout << cnt << endl;
    }
 
}
