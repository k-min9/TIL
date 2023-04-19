def solution(n):
	answer = ''
	for i in range(n):
		answer += str((i+1)%9)
		answer = answer[::-1]
	return answer