'''
이거 제대로 풀면 수식이나 DP로 엄청 깔끔히 풀 수 있음.
요는 시간 신경 쓸 필요 없다는 소리
'''
DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def solution(n):
	answer = 0
	arr = [[0]*n for _ in range(n)]
	
	direction = 0
	x = -1
	y = 0
	for i in range(n*n):
		nx = x + DIR[direction][0]
		ny = y + DIR[direction][1]
		if not (0<=nx<n and 0<=ny<n and arr[ny][nx] == 0):
			direction = (direction+1)%4
		x += DIR[direction][0]
		y += DIR[direction][1]
		arr[y][x] = i+1	

	for i in range(n):
		answer += arr[i][i]
	
	return answer