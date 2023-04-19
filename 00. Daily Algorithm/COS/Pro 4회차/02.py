'''
15번째 줄, s[0]를 alphabet으로
'''
def solution(s):
	s = s.lower()
	answer = ""
	previous = s[0]
	counter = 1
	for alphabet in s[1:]:
		if alphabet == previous:
			counter += 1
		else:
			answer += previous + str(counter)
			counter = 1
			previous = alphabet
	answer += previous + str(counter)
	return answer
