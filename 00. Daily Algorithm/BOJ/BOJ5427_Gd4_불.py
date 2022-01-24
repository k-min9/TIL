'''
BFS 
1. 불 이동이 먼저
2. 상근이 이동이 다음
>> 레퍼런스 : 실제로는 불이 그곳까지 걸리는 시간 체크하는 방식으로 
복습하는 느낌으로 라이브 코딩
'''
import sys
from collections import deque
input = sys.stdin.readline

# 상수
MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]
 
 
def fire():
    fqlen = len(fire_queue)
    while fqlen:
        x, y = fire_queue.popleft()
        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    fire_queue.append((nx, ny))
        fqlen -= 1
 
 
def bfs(i, j):
    queue.append((i, j))
    visited[i][j] = 1
    while queue:
        qlen = len(queue)
        while qlen:
            x, y = queue.popleft()
            for dx, dy in MOVES:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                    if graph[nx][ny] == '.':
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
                elif nx < 0 or ny < 0 or nx >= h or ny >= w:
                    print(visited[x][y])
                    return
            qlen -= 1
        fire()
    print("IMPOSSIBLE")
    return
 
 
for _ in range(int(input())):
    w, h = map(int, input().split())
    graph = [list(input().strip()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
 
    queue, fire_queue = deque(), deque()
 
    for x in range(h):
        for y in range(w):
            if graph[x][y] == '@':
                start_x, start_y = x, y
                graph[x][y] = '.'
            if graph[x][y] == '*':
                fire_queue.append((x, y))
    fire()
    bfs(start_x, start_y)
