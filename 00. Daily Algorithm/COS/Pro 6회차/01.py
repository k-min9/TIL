from collections import deque

MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def solution(n, garden):
	answer = 0
	
	queue = deque()
	
	for x in range(n):
		for y in range(n):
			if garden[y][x] == 1:
				queue.append((x, y))
	
	while queue:
		x, y = queue.popleft()
		for dx, dy in MOVES:
			nx = x + dx
			ny = y + dy
			if 0<=nx<n and 0<=ny<n and garden[ny][nx] == 0:
				garden[ny][nx] = garden[y][x] + 1
				queue.append((nx, ny))
				answer = max(answer, garden[y][x])
	
	return answer