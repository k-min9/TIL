import sys
sys.stdin = open('input.txt')

# 상수
moves = ((1, 0), (0, 1), (-1, 0), (0, -1))


def find_start():
    for y in range(N):
        for x in range(N):
            if graphs[y][x] == '2':
                return y, x


def dfs(y, x):
    global answer

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
            # 도착
            if graphs[ny][nx] == '3':
                answer = 1
            elif graphs[ny][nx] == '0':
                visited[ny][nx] = 1
                dfs(ny, nx)


T = int(input())
for t in range(T):

    N = int(input())
    graphs = [input().rstrip() for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    y, x = find_start()
    answer = 0
    dfs(y, x)

    print(f'#{t+1}', answer)
