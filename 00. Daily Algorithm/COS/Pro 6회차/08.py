def solution(S):
	check = func_b(S)
	dp = func_a(check)
	answer = func_c(dp)
	return answer