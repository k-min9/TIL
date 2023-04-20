'''
dp 1줄
'''
def solution(n):
	answer = 0
	steps = [0 for _ in range(n+1)]
	steps[1] = 1
	steps[2] = 2
	steps[3] = 4
	for i in range(4, n+1):
		steps[i] = steps[i-1] + steps[i-2] + steps[i-3]
	answer = steps[n]
	return answer