def solution(commands):
	answer = [0, 0]
	for c in commands:
		if c == "U":
			answer[1] += 1
		elif c == "D":
			answer[1] -= 1
		elif c == "R":
			answer[0] += 1
		elif c == "L":
			answer[0] -= 1	
	return answer
