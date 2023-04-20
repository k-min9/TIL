'''
한줄 수정 : right = len(numbers) - 1 이 아니라 -2
'''

def solution(numbers):
	answer = []
	numbers.sort()
	mid = (len(numbers) - 1) // 2
	numbers[mid], numbers[len(numbers)-1] = numbers[len(numbers)-1], numbers[mid]
	left = mid + 1
	right = len(numbers) - 2
	while left <= right:
		numbers[left], numbers[right] = numbers[right], numbers[left]
		left = left + 1
		right = right - 1
	answer = numbers
	return answer