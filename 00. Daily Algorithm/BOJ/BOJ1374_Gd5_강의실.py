'''
강의 번호 필요 없지 않나....?
강의실이니까 일단 받아서 소트하고... 
종료시간이 10억이니까 시간순 진행하면 안되고 소트한거 뽑아야됨
뭐할지는 그때가서 생각해야될듯
'''
import sys
input = sys.stdin.readline
from collections import deque

# 강의 개수
N = int(input())
lectures_start = list()
lectures_end = list()
for _ in range(N):
    num, s, e = map(int, input().split())
    lectures_start.append(s)
    lectures_end.append(e)
lectures_start = deque(sorted(lectures_start))
lectures_end = deque(sorted(lectures_end))

cnt = 0
answer = 0
while lectures_start:
    if lectures_start[0] < lectures_end[0] :
        cnt += 1
        answer = max(answer, cnt)
        time = lectures_start.popleft()
    else:
        time = lectures_end.popleft()
        cnt -= 1
print(answer)

'''
정수기 뜨거운물, 찬물 돌아가면서 뽑아 먹듯이 뽑으니까 끝남
'''