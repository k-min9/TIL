'''
이동하기 위한 최소 이동 횟수 => BFS가 제일 깔끔할 듯
'''
from collections import deque
import sys
input = sys.stdin.readline

# 상수
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 사각형이 벽에 걸렸는지 여부
def check(y, x):
    for wy, wx in walls:
        if y<=wy<y+H and x<=wx<x+W:
            return False
    return True

def bfs():
    que = deque()
    que. append((Sr-1, Sc-1, 0))

    while que:
        y, x, cnt = que.popleft()
        visited[y][x] = 1

        if y == Fr-1 and x == Fc-1:
            print(cnt)
            return
        
        for dx, dy in MOVES:
            ny = y + dy
            nx = x + dx

            if 0<=ny<N and 0<=nx<M and 0 <= ny + H - 1 < N and 0 <= nx + W - 1 < M:
                if not visited[ny][nx]:
                    if check(ny, nx):
                        visited[ny][nx] = 1
                        que.append((ny, nx, cnt+1))
    print(-1)
    return

# 입력
N, M = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(N)]
# 직사각형의 크기 H, W 시작 좌표 Sr Sc 도착 좌표 Fr Fc
H, W, Sr, Sc, Fr, Fc = map(int, input().split())

visited = [[0]*M for _ in range(N)]
walls = list()
for i in range(N):
    for j in range(M):
        if graphs[i][j] == 1:
            walls.append((i, j))

bfs()
