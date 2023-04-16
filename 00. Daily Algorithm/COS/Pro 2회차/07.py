def solution(money):
	coin = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
	counter = 0
	idx = len(coin) - 1
	while money:
		counter += money // coin[idx]
		money %= coin[idx]
		idx -= 1
	return counter
