def solution(phrases, second):
	answer = ''
	second = second % 28
	if second <= 14:
		answer = '_'*(14-second) + phrases[:second]
	else:
		answer = phrases[second-14:] + '_'*(28-second)
	
	return answer
