'''
접근 > 삼성 기출문제 : 시험문제 풀듯이 풀자.
완전 탐색 > 백트래킹 없음 > BFS
'''
import sys
from collections import deque
input = sys.stdin.readline

# 상수
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(i, j):
    if visited[i][j] == 1:
        return

    global flag
    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    union = list()
    union.append((i, j))

    while(q):
        x, y = q.popleft()
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and L<=abs(graph[nx][ny] - graph[x][y])<=R:
                q.append((nx, ny))
                union.append((nx, ny))
                visited[nx][ny] = 1
                flag = True

    if len(union) >= 2:
        avg = 0
        for x, y in union:
            avg += graph[x][y]
        avg = avg//len(union)
        for x, y in union:
            graph[x][y] = avg


N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 인구 이동 종료 여부
flag = True

# 방문 여부
visited = [[0]*N for _ in range(N)]

answer = 0
while(flag):
    flag = False
    # 방문, 연합, 분배까지
    for i in range(N):
        for j in range(N):
            bfs(i, j)
    # 카운트 여부(이동수 올리고, 초기화)
    if flag == True:
        answer = answer + 1
        visited = [[0]*N for _ in range(N)]

print(answer)
