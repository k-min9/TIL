def solution(num):
	next_num = num
	while True:
		next_num += 1
		length = func_b(next_num)
		if length % 2:
			continue
		divisor = func_a(length//2)  
		front = next_num // divisor
		back = next_num % divisor

		front_sum = func_c(front)
		back_sum = func_c(back)
		if front_sum == back_sum:
			break
	return next_num - num