def solution(arrA, arrB):
	if len(arrA) != len(arrB):
		return False
	if func_b(arrA, arrB):
		arrA_temp = func_a(arrA)
		if func_c(arrA_temp, arrB):
			return True
	return False
