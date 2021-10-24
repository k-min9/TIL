#include <iostream>

using namespace std;

bool visited[9];
bool conflict[9][9];
int answer = 0;
int idx = 0;

struct friends_pair {
	int a, b;
};


void dfs(int x){
	visited[x] == 1;
	idx++;

	if (idx == 8) {
		answer++;
		visited[x] = 0;
		idx--;
		return;
	}

	for (int i = 1; i <= 8; i++){
		if (!visited[i] && !conflict[x][i]){
			dfs(i);
		}
	}

	visited[x] =0;
	idx--;
}

void solution(int n, friends_pair * pairs) {

	for (int i = 0 ; i < n ; i ++)
	{
		conflict[pairs[i].a][pairs[i].b] = 1;
		conflict[pairs[i].b][pairs[i].a] = 1;
	}

	for (int i = 1; i <= 8; i++)
	{
		dfs(i);
	}
	cout << answer;
}