'''
여기까지 600점. 현재 기량으로 15분 정도 걸림
'''
DIR = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
def solution(pos):
	x = 0
	y = 0
	if pos[0] == "A":
		x = 1
	elif pos[0] == "B":
		x = 2
	elif pos[0] == "C":
		x = 3
	elif pos[0] == "C":
		x = 4
	elif pos[0] == "D":
		x = 5
	elif pos[0] == "E":
		x = 6
	elif pos[0] == "F":
		x = 7
	elif pos[0] == "G":
		x = 8
	y = int(pos[1])
	
	answer = 0
	for dx, dy in DIR:
		if 1<=x+dx<=8 and 1<=y+dy<=8:
			answer += 1
		
	return answer