import sys
sys.stdin = open('input.txt')

#상수
MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def find_starts():
    height_max = 1
    starts = list()
    for y in range(N):
        for x in range(N):
            if height_max < graphs[y][x]:
                height_max = graphs[y][x]
                starts = list()
            if height_max == graphs[y][x]:
                starts.append((x, y))
    return starts


def dfs(x, y, K, length):
    global answer
    answer = max(answer, length)

    for dx, dy in MOVES:
        nx = x + dx
        ny = y + dy
        if 0<=nx<N and 0<=ny<N and not visited[ny][nx]:
            # 이동 가능시 그냥 이동
            if graphs[ny][nx] < graphs[y][x]:
                visited[ny][nx] = 1
                dfs(nx, ny, K, length + 1)
                visited[ny][nx] = 0
            # 이동 불가시(나머지) & 아직 공사찬스 있음
            elif K != 0:
                # 현재 높이 - 1 까지 공사 & 공사 찬스 소멸
                if graphs[ny][nx] < graphs[y][x] + K:
                    tmp = graphs[ny][nx]
                    graphs[ny][nx] = graphs[y][x] - 1
                    visited[ny][nx] = 1
                    dfs(nx, ny, 0, length + 1)
                    # 공사전 까지 복구
                    visited[ny][nx] = 0
                    graphs[ny][nx] = tmp


for t in range(int(input())):
    N, K = map(int, input().split())
    graphs = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    for x, y in find_starts():
        visited = [[0] * N for _ in range(N)]
        visited[y][x] = 1
        dfs(x, y, K, 1)

    print(f'#{t+1}', answer)
