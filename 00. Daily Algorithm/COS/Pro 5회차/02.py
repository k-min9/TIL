'''
한줄 수정 : 큰거작은거 위치변경
'''
def solution(walls):
	answer = 0
	for i in range(len(walls)):
		for j in range(i+1, len(walls)):
			area = 0
			if walls[i][1] <= walls[j][1]:
				area = walls[i][1] * (walls[j][0] - walls[i][0])
			else:
				area = walls[j][1] * (walls[j][0] - walls[i][0])
			if answer < area:
				answer = area
	return answer