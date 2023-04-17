'''
break를 continue로
'''
def solution(k, student):
	answer = 0
	for s in student:
		s -= 4*k
		if s <= 0:
			continue
		answer += (s + k - 1) // k
	return answer
