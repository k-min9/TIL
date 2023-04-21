def solution(K, numbers, up_down):
	left = 1
	right = K
	for num, word in zip(numbers, up_down):
		if word == "UP":
			left = max(left, num+1)
		elif word == "DOWN":
			right = min(right,num-1)
		elif word == "RIGHT":
			return 1
	return right-left+1