'''
길이 = 일단 BFS
'''
from collections import deque
import sys
input = sys.stdin.readline


# 상수
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:    
        x, y = queue.popleft()
    
        for dx, dy in MOVES:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M or graphs[nx][ny] == 0:
                continue

            if graphs[nx][ny] == 1:
                graphs[nx][ny] = graphs[x][y] + 1
                queue.append((nx, ny))
    
    return graphs[N-1][M-1]

N, M = map(int, input().split())
graphs = [list(map(int, input().strip())) for _ in range(N)]

print(bfs(0, 0))

'''
좋은 몸풀이
'''