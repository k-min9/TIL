'''
range(len(revenue)를 range(k, len(revenue))로
'''
def solution(revenue, k) :
	answer = 0
	rsum = sum(revenue[0:k])
	answer = rsum
	for i in range(k, len(revenue)) :
		rsum = rsum - revenue[i - k] + revenue[i]
		if answer < rsum :
			answer = rsum
	return answer