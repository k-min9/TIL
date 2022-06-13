'''
적록색약이면 R과 G 통합이 가능. 끝
'''
from collections import deque

MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(x, y):
    q.append([x, y])
    c[x][y] = cnt
    while q:
        x, y = q.popleft()
        for dx, dy in MOVES:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if a[nx][ny] == a[x][y] and c[nx][ny] == 0:
                    q.append([nx, ny])
                    c[nx][ny] = 1


N = int(input())
a = [list(map(str, input())) for _ in range(N)]
c = [[0]*N for _ in range(N)]
q = deque()

# 일반
cnt = 0
for i in range(N):
    for j in range(N):
        if c[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt, end=' ')

# R -> G 로 변환
for i in range(N):
    for j in range(N):
        if a[i][j] == 'R':
            a[i][j] = 'G'
c = [[0]*N for _ in range(N)]

# 적록색약
cnt = 0
for i in range(N):
    for j in range(N):
        if c[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)
