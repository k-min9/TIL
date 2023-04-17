MOVES = [(-1, 1), (1, 1), (-1, -1), (1, -1)]

def solution(bishops):
	def func1(x, y):
		for dx, dy in MOVES:
			nx = x
			ny = y
			while 1<=nx<=8 and 1<=ny<=8:
				b_set.add((nx, ny))
				nx += dx
				ny += dy
		
	b_set = set()
	for bishop in bishops:
		x = ord(bishop[0]) - (ord('A') - 1)
		y = int(bishop[1])
		func1(x, y)		

	return 64-len(b_set)
