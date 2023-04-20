'''
q진법 관련 파이썬 함수
10 -> 2,8,16 : bin, oct, hex
'''
def chngToQ(num, q):
	ret = ''
	while num:
		ret = str(num%q) + ret
		num //= q
	return ret

def solution(s1, s2, p, q):
	answer = ''
	a = int(s1, p) + int(s2, p)
	return chngToQ(a, q)
