def power(base, exponent):
	val = 1
	for i in range(exponent):
		val *= base
	return val

def solution(k):
	answer = []
	bound = power(10, k)
	for i in range(bound // 10, bound):
		current = i
		calculated = 0
		while current != 0:
			calculated += power(current%10, k)
			current //= 10			
		if calculated == i:
			answer.append(i)
	return answer