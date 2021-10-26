#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main() 
{
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	// string input; 
	// cin >> input;
	

  // vector, 내용 추가, 소트
	vector<int> nums(6, 0);
	for (int i = 0; i < nums.size() ; i++)
	{
		nums[i] = i + 1;
	}
	nums.push_back(3);
	sort(nums.begin(),nums.end());

	// 1차원 배열 출력
	for (int i: nums)
	{
    std::cout << i << ' ';
	}

	return 0;
}