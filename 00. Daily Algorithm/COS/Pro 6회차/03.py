def solution(arr, K):
	answer = 987654321
	arr.sort()
	for i in range(len(arr)-K+1):
		answer = min(answer, arr[i+K-1]-arr[i])
	
	return answer
