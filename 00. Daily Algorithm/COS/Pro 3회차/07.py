'''
한 줄 :
square_num % divisor != 0를 square_num // divisor != 0로
'''
def solution(k):
	answer = []
	for i in range(1, k + 1):
		square_num = i * i
		divisor = 1
		while square_num // divisor != 0:
			front = square_num // divisor
			back = square_num % divisor
			divisor *= 10
			if back != 0 and front != 0:
				if front + back == i:
					answer.append(i)
	return answer
