// 언어 : cpp, BFS
#include <iostream>
#include <queue>

using namespace std;

int tomatoMap[1000][1000];
queue<pair<int, int>> q;
int result = 0;
int M, N;
int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

void BFS() {
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;

		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx >= 0 && ny >= 0 && nx < N && ny < M) {
				if (tomatoMap[nx][ny] == 0) {
					tomatoMap[nx][ny] = tomatoMap[x][y] + 1;
					q.push(make_pair(nx, ny));
				}
			}
		}
	}
}

void tomato() {
	cin >> M >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> tomatoMap[i][j];

			if (tomatoMap[i][j] == 1) {
				q.push(make_pair(i, j));
			}
		}
	}

	BFS();

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (tomatoMap[i][j] == 0) {
				cout << -1 << "\n";
				return;
			}

			if (result < tomatoMap[i][j]) {
				result = tomatoMap[i][j];
			}
		}
	}

	cout << result - 1 << "\n";
}

int main() {
	tomato();

	return 0;
} 