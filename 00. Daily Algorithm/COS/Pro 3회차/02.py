def solution(s, k):
	palindromes = []
	length = len(s)
	for start_idx in range(length):
		for cnt in range(1, length - start_idx + 1):
			sub_s = s[start_idx : start_idx + cnt]
			if func_b(sub_s) == True:
				if func_a(palindromes, sub_s) == False:
					palindromes.append(sub_s)

	answer = func_c(palindromes, k)
	return answer
