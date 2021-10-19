'''
DFS 체크
'''
import sys
input = sys.stdin.readline

# 상수
MOVES = ((-1, 0), (1, 0), (0, 1), (0, -1))


def dfs(x, y, depth):
    global answer
    answer = max(answer, depth)

    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy

        if 0<=nx<C and 0<=ny<R and not visited[ny][nx] and maps[ny][nx] not in check_set:
            visited[ny][nx] = 1
            check_set.add(maps[ny][nx])
            dfs(nx, ny, depth + 1)
            visited[ny][nx] = 0
            check_set.remove(maps[ny][nx])


# 세로, 가로
R, C = map(int, input().split())
maps = [input().rstrip() for _ in range(R)]
visited = [[0]*C for _ in range(R)]

answer = 1
check_set = {maps[0][0]}  # 중복 체크용
dfs(0, 0, 1)
print(answer)
