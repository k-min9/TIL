'''
left % 2 == 0: -> idx % 2 ==0
'''
def solution(arr):
	left, right = 0, len(arr) - 1
	idx = 0
	answer = [0 for _ in range(len(arr))]
	while left <= right:
		if idx % 2 == 0:
			answer[idx] = arr[left]
			left += 1
		else:
			answer[idx] = arr[right]
			right -= 1
		idx += 1
	return answer
