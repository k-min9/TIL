#include <iostream>
#include <string>
#include <set>

using namespace std;

struct query {
	string operation;
	int branchNum;
};

void solution(int n, query * queries) {
	
	set<int> answers;
	set<int> nexts;

	answers.insert(1);

	for (int i = 0; i < n ; i++)
	{
		if (queries[i].operation == "branch"){
			if (nexts.empty()){
				int next = *answers.rbegin() + 1;
				answers.insert(next);
			}
			else{
				int next = *nexts.begin();
				nexts.erase(next);
				answers.insert(next);
			}
		}
		else{
			int er = queries[i].branchNum;
			answers.erase(er);
			nexts.insert(er);
		}
	}

	for (int answer : answers)
	{
		cout << answer << " ";
	}
}