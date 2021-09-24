import sys
sys.stdin = open('input.txt')
from collections import deque

# 상수
MOVES = [(0, -1), (-1, 0), (0, 1), (1, 0)] # 상좌하우(dx, dy)
TUNNELS = [(), (0, 1, 2, 3), (0, 2), (1, 3), (0, 3), (2, 3), (1, 2), (0, 1)]


def bfs(x, y):
    if L == 1:
        return 1
    visited = [[0]*M for _ in range(N)]
    visited[y][x] = 1

    que = deque()
    que.append((x, y))
    answer = 1
    while que:
        x, y = que.popleft()
        for dir in TUNNELS[graphs[y][x]]:
            dx, dy = MOVES[dir]
            nx = x + dx
            ny = y + dy
            if 0<=nx<M and 0<=ny<N and not visited[ny][nx] and (dir+2)%4 in TUNNELS[graphs[ny][nx]]:
                answer += 1
                visited[ny][nx] = visited[y][x] + 1
                if visited[ny][nx] < L:
                    que.append((nx, ny))
    # for v in visited:
    #     print(*v)
    return answer


for t in range(int(input())):
    # 세로, 가로, 맨홀y, 맨홀x, 시간
    N, M, R, C, L = map(int, input().split())
    graphs = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{t+1}', bfs(C, R))
