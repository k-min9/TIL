'''
몇번 움직여야 이동할 수 있을까? => BFS로 접근
'''
import sys
input = sys.stdin.readline
from collections import deque


# 상수
MOVES = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2,1)]


# 함수
def bfs(sx, sy, ex, ey):

    que = deque()
    que.append((sx, sy))
    visited[sx][sy] = 1

    while que:
        x, y = que.popleft()
        if x == ex and y == ey:
            print(visited[x][y]-1)
            return
        for dx, dy in MOVES:
            nx = x + dx
            ny = y + dy
            if 0<=nx<l and 0<=ny<l and visited[nx][ny] == 0:
                que.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1  


for _ in range(int(input())):

    # 한 변 길이, 스타트, 목적지
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    # 계산
    visited = [[0]*l for i in range(l)]
    bfs(sx, sy, ex, ey)
    