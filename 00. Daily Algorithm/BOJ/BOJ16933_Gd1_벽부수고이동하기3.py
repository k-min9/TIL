'''
최단 경로 = bfs 내지 backtrack dfs(거리 갱신 귀찮음)
수정 >> 최단 경로 수 인줄 알았는데 경로 길이면 그냥 bfs
추가로 보낼 인자(벽 부수기 찬스 횟수, 낮/밤 상태) 
'''
import sys
input = sys.stdin.readline
from collections import deque

# 상수
MOVES = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs():
    # 초기화 (x좌표, y좌표, 찬스 횟수, 낮(1)/밤(0)), 거리
    q = deque()
    q.append((0, 0, K, 1, 0))
    # 방문
    visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
    visited[0][0][K] = 1

    while q:
        x, y, chance, breakable, dist = q.popleft()
        if x == M-1 and y == N-1:
            return dist + 1
        for dx, dy in MOVES:
            nx = x + dx
            ny = y + dy
            if 0<=nx<M and 0<=ny<N:
                # 벽 아님(그냥 이동)
                if maps[ny][nx] == '0':
                    if not visited[ny][nx][chance]:
                        visited[ny][nx][chance] = 1
                        q.append((nx, ny, chance, (breakable + 1) % 2, dist+1))
                # 벽 이지만 찬스 남음
                elif chance:
                    if not visited[ny][nx][chance-1]:
                        # 낮이냐
                        if breakable:
                            visited[ny][nx][chance-1] = 1
                            q.append((nx, ny, chance-1, (breakable + 1) % 2, dist+1))
                        # 밤이면 대ㅡ기 하고 시간만 경과
                        else:
                            q.append((x, y, chance, (breakable + 1) % 2, dist+1))

    return -1
                  
# 세로, 가로, 벽 부수기 찬스(낮)
N, M, K = map(int, input().split())
maps = [input().rstrip() for _ in range(N)]

print(bfs())