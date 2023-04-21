'''
coins[i][j] = board[i][j] + max(coins[i][j], coins[i-1][j-1])를
coins[i][j] = board[i][j] + max(coins[i-1][j], coins[i][j-1])로
'''
def solution(board):
	coins = [[0 for c in range(4)] for r in range(4)]
	for i in range(4):
		for j in range(4):
			if i == 0 and j == 0:
				coins[i][j] = board[i][j]
			elif i == 0 and j != 0:
				coins[i][j] = board[i][j] + coins[i][j-1]
			elif i != 0 and j == 0:
				coins[i][j] = board[i][j] + coins[i-1][j]
			else:
				coins[i][j] = board[i][j] + max(coins[i-1][j], coins[i][j-1])
	answer = coins[3][3]
	return answer
