'''
가로로 접냐 세로로 접냐인데
진짜 더럽게 못짰다.
'''
def solution(grid):
	answer = 0
	for i in range(4):
		for j in range(4):
			for k in range(j + 1, 4, 2):
				answer = max(answer, max(grid[i][j] + grid[j][k], grid[i][j] + grid[k][i]))
	return answer