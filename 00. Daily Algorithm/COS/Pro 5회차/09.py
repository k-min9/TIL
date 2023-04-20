from collections import deque

def solution(number, target):
	dp = [-1] * 10001
	dp[number] = 0
	if number == target:
		return 0
	
	q = deque([number])	
	while True:
		num = q.popleft()
		
		if 0<=num+1<=10000:
			if num+1 == target:
				return dp[num]+1
			dp[num+1] = dp[num]+1
			q.append(num+1)
		
		if 0<=num-1<=10000:
			if num-1 == target:
				return dp[num]+1
			dp[num-1] = dp[num]+1
			q.append(num-1)
			
		if 0<=num*2<=10000:
			if num*2 == target:
				return dp[num]+1
			dp[num*2] = dp[num]+1
			q.append(num*2)		
