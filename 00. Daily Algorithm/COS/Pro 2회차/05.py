'''
이거 말고 LIS인가 그거가 기억이 안나는데 잠만...
가장 긴 증가하는 부분 수열 : 이진탐색 사용시 O(NlogN)인데 거기까지도 필요 없음
'''
def solution(arr):
	answer = 0
	last_num = 0
	now_len = 0
	for a in arr:
		if a > last_num:
			now_len += 1
		else:
			now_len = 1
		answer = max(answer, now_len)
		last_num = a
		
	return answer