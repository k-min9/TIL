'''
덩어리 찾기면 걍 DFS 써도 되고 흐음...
'''
import sys
input = sys.stdin.readline
from collections import deque


MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(x, y):
    cnt = 1
    queue = deque()
    queue.append((x, y))
    graphs[x][y] = 0

    while queue:
        x, y  = queue.popleft()

        for dx, dy in MOVES:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if graphs[nx][ny] == 1:
                    graphs[nx][ny] = 0
                    queue.append((nx, ny))
                    cnt += 1
    
    return cnt


N, M, K = map(int, input().split())
graphs = [[0]*M for _ in range(N)]
for i in range(K):
    r, c = map(int, input().split())
    graphs[r-1][c-1] = 1

answer = 0
for x in range(N):
    for y in range(M):
        if graphs[x][y] == 1:
            answer = max(answer, bfs(x, y))

print(answer)
