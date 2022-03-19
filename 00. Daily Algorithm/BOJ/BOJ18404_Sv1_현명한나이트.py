'''
최소의 수 = BFS

'''
import sys
from collections import deque
input = sys.stdin.readline


# 상수
MOVES = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    graphs[y][x] = 0
    while q:
        y, x = q.popleft()
        for dy, dx in MOVES:
            nx = x+dx
            ny = y+dy
            if (0 <= ny < N) and (0 <= nx < N) and graphs[ny][nx] == -1:
                q.append((ny, nx))
                graphs[ny][nx] = graphs[y][x]+1

# 체스판 크기, 잡아야할 말의 수s
N, M = map(int, input().split())

# 시작점
sy, sx = map(int, input().split())
graphs = [[-1]*N for _ in range(N)]  # 해당 지점으로 가기 위해 필요한 이동수
knights = [list(map(int, input().split())) for _ in range(M)]  # 나이트 위치

bfs(sy-1, sx-1)
for y, x in knights:
    print(graphs[y-1][x-1], end=' ')
