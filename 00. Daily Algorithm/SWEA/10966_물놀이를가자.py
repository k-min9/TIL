import sys
sys.stdin = open('input.txt')
from collections import deque

# 상수
MOVES = [(0, -1), (-1, 0), (0, 1), (1, 0)]

for t in range(int(input())):
    # 세로, 가로
    N, M = map(int, input().split())
    graphs = [input().rstrip() for _ in range(N)]

    visited = [[-1] * M for _ in range(N)]
    que = deque()
    for y in range(N):
        for x in range(M):
            if graphs[y][x] == "W":
                visited[y][x] = 0
                que.append((x, y, 0))

    while que:
        x, y, dist = que.popleft()
        for dx, dy in MOVES:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == -1:
                visited[ny][nx] = dist + 1
                que.append((nx, ny, dist + 1))

    answer = 0
    for v in visited:
        answer += sum(v)

    print(f'#{t+1}', answer)
