#include <iostream>
#include <unordered_map>
#include <queue>

using namespace std;

void solution(int n, int k, int * numOfFrequenciesInRegion, int ** frequencies) {

	int answer = 0;
	unordered_map<int, int> count;
	priority_queue <pair <int, int>> chk;

	for (int i = 0 ; i < n ; i ++)
	{
		for (int j = 0 ; j < numOfFrequenciesInRegion[i] ; j++)
		{
			count[frequencies[i][j]]++;
		}
	}

	for (auto itr : count)
	{
		chk.push({itr.second, itr.first});
	}

	for (int i = 0; i < k ; i++)
	{
		answer += chk.top().first;
		chk.pop();
	}

	cout << answer;
}