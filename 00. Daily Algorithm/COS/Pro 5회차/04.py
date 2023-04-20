'''
한줄 수정 : range(10)에서 range(9,-1,-1) 로
'''

def solution(number):
	answer = ''
	number_count = [0 for _ in range(10)]
	while number > 0:
		number_count[number % 10] += 1
		number //= 10
	for i in range(9,-1,-1):
		if number_count[i] != 0:
			answer += (str(i) + str(number_count[i]))
	return answer