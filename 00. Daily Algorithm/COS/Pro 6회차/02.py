def solution(K, words):
	words_len = list()
	for word in words:
		words_len.append(len(word)+1)
	words_len[0] -= 1
	
	answer = 1
	x = 10
	for word_len in words_len:
		if x >= word_len:
			x -= word_len
		else:
			answer += 1
			x = 10 - word_len
	
	return answer
