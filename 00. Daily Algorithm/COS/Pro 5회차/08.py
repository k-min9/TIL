def func_a(a, b):
	mod = a % b
	while mod > 0:
		a = b
		b = mod
		mod = a % b
	return b

def func_b(n):
	answer = 0
	for i in range(1, n+1):
		if func_c(n, i):
			answer += 1
	return answer

def func_c(p, q):
	if p % q == 0:
		return True
	else:
		return False

def solution(a, b, c):
	answer = 0
	gcd = func_a(func_a(a, b), c)
	answer = func_b(gcd)
	return answer