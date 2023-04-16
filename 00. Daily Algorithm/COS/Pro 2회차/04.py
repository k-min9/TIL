from itertools import combinations

def solution(arr, K):
	answer = 0
	for comb in combinations(arr, 3):
		if sum(comb)%K == 0:
			answer += 1
	
	return answer
