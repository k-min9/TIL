import sys
sys.stdin = open('input.txt')
from collections import deque

# 상수
moves = ((1, 0), (0, 1), (-1, 0), (0, -1))


def find_start():
    for y in range(N):
        for x in range(N):
            if graphs[y][x] == '2':
                return y, x


def bfs(y, x):

    q = deque()
    q.append((y, x))
    visited = [[0]*N for _ in range(N)]
    visited[y][x] = 1
    answer = 0

    while q:
        y, x = q.popleft()

        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                # 도착
                if graphs[ny][nx] == '0':
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))
                elif graphs[ny][nx] == '3':
                    answer = visited[y][x] - 1

    return answer


T = int(input())
for t in range(T):

    N = int(input())
    graphs = [input().rstrip() for _ in range(N)]

    y, x = find_start()
    answer = bfs(y, x)

    print(f'#{t+1}', answer)
