'''
solution 구현하기 : 3초
'''
def solution(num):
	answer = num + 1
	while '0' in str(answer):
		answer += 1
	return answer
 
num = 9949999;
ret = solution(num)
 
print("solution 함수의 반환 값은", ret, "입니다.")