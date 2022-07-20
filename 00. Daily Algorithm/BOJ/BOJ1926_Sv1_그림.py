'''
전형적인 BFS 문제 0분침하는거 보여드림
'''
import sys
input = sys.stdin.readline
from collections import deque


MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    graphs[x][y] = 0
    size = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in MOVES:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < M and graphs[nx][ny] == 1:
                size += 1
                graphs[nx][ny] = 0
                queue.append([nx, ny])

    answers.append(size)


N, M = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(N)]

answers = list()
for x in range(N):
    for y in range(M):
        if graphs[x][y] == 1:
            bfs(x, y)

print(len(answers))
if len(answers) != 0:
    print(max(answers))
else:
    print(0)

'''
ㅎㅎㅎ!
'''