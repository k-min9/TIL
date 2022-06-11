'''
방문까지의 최소 거리 = BFS 인데 빛이라 살짝 변형
'''
from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y, dir):
    q.append([x, y, dir])
    visited[x][y][dir] = 1
    ans = []
    while q:
        x, y, dir = q.popleft()
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < n and 0 <= ny < n:
            # 미방문 내지 방문까지 필요 횟수 갱신
            if not visited[nx][ny][dir] or visited[nx][ny][dir] > visited[x][y][dir]:
                if a[nx][ny] != '*':
                    visited[nx][ny][dir] = visited[x][y][dir]
                    # 방문한 곳이 문
                    if nx == fx and ny == fy:
                        ans.append(visited[nx][ny][dir])
                        continue
                    q.append([nx, ny, dir])
                    # 방문한 곳이 ! (거울 설치 가능 구역)
                    if a[nx][ny] == '!':
                        turn(nx, ny, dir)

    return min(ans) - 1

# 90도 방향 전환
def turn(x, y, dir):
    ndir = [(dir+1) % 4, (dir+3) % 4]
    for d in ndir:
        if not visited[x][y][d] or visited[x][y][d] > visited[x][y][dir] + 1:
            visited[x][y][d] = visited[x][y][dir] + 1
            q.append([x, y, d])

n = int(input())
q = deque()
visited = [[[0]*4 for _ in range(n)] for _ in range(n)]  # 방문과 방문까지의 거리를 겸용

# 문 찾기
a, temp = [], []
for i in range(n):
    row = list(input().strip())
    a.append(row)
    for j in range(n):
        if row[j] == '#':
            temp.extend([i, j])
sx, sy, fx, fy = temp

# 문에서 어디로 이동할 수 있는지
for i in range(4):
    nx = sx + dx[i]
    ny = sy + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
        if a[nx][ny] != '*':
            dir = i
            break

print(bfs(sx, sy, dir))
