'''
원래는 뒤집어서 해야됨
'''
def solution(s1, s2):
	answer = 0
	len_s1 = len(s1)
	len_s2 = len(s2)
	len_s = min(len_s1, len_s2)
	
	# s1에 s2 합치기
	for i in range(len_s):
		if s1[:i+1] == s2[-1-i:]:
			answer = max(answer, i+1)
		if s2[:i+1] == s1[-1-i:]:
			answer = max(answer, i+1)
	
	return len_s1 + len_s2 - answer
