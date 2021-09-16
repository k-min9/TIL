'''
상어 특) 라이브러리 봉인
N = 20, 2초 >> 하고 싶은거 다 해
'''

import sys
from collections import deque
input = sys.stdin.readline

# 상수
MOVES = [(1,0),(-1,0),(0,1),(0,-1)]

# 상어 위치
def find_shark():
    for y in range(N):
        for x in range(N):
            if maps[y][x] == 9:
                maps[y][x] = 0
                return x, y

# 상어의 위치 값을 받고, 먹을 수 있는 물고기 리스트 중 최적값을 반환(BFS)
def next_fish(x, y):
    q = deque()
    q.append((0, x, y))
    visited = [[0]*N for _ in range(N)]
    visited[y][x] = 1
    
    # 물고기 리스트 물색
    targets = list()
    while q:
        dist, x, y  = q.popleft()
        dist += 1
        for dx, dy in MOVES:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N and not visited[ny][nx]:
                # 지나갈수 있음?
                if 0 <= maps[ny][nx] <= shark_size:
                    q.append((dist, nx, ny))
                    visited[ny][nx] = 1
                    # 그 와중에 물고기 확보
                    if 1 <= maps[ny][nx] < shark_size:
                        targets.append((dist, nx, ny))
    # 먹을게 있니?
    if len(targets):
        targets.sort(key = lambda x : (x[0],x[2],x[1]))
        maps[targets[0][2]][targets[0][1]] = 0
        # 냠냠 먹기
        eat_fish()
        return targets[0]
    else:
        return None

def eat_fish():
    global shark_exp, shark_size
    shark_exp += 1
    if shark_size == shark_exp:
        shark_exp = 0
        shark_size += 1

# 상어 정보
shark_size = 2
shark_exp = 0

# 시작 
N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

x, y = find_shark()

answer = 0
while True:
    target = next_fish(x, y)
    if target:
        dist, x, y = target
        answer += dist
    else:
        break
print(answer)
