import sys
sys.stdin = open('input.txt')

# 상수
moves = ((1, 0), (0, 1), (-1, 0), (0, -1))


def find_start():
    for y in range(16):
        for x in range(16):
            if graphs[y][x] == '2':
                return y, x


def dfs(y, x):
    global answer

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 16 and 0 <= ny < 16 and not visited[ny][nx]:
            # 도착
            if graphs[ny][nx] == '3':
                answer = 1
            elif graphs[ny][nx] == '0':
                visited[ny][nx] = 1
                dfs(ny, nx)


for t in range(10):

    trash = int(input())
    graphs = [input().rstrip() for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]

    y, x = find_start()
    answer = 0
    dfs(y, x)

    print(f'#{t+1}', answer)
