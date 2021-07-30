'''
쉽다가 무슨 뜻이더라
아마 BFS 쪽이 빠를거라고 생각함.
'''
import sys
input = sys.stdin.readline
from collections import deque  # BFS! BFS!

# BFS
def BFS(startX, startY):
    q = deque()
    q.append([startX, startY])
    graph[startX][startY] = 0
    while q:
        x, y = q.popleft()
        # 이동해서 체크
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = 1
                graph[nx][ny] = graph[x][y] + 1
        

# N이 세로 M이 가로
N, M = map(int, input().split())

# 죄다 1 빼면 visited 함수를 만들 수 있다.
visited = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]
graph = [[-1]*M for _ in range(N)]

# 문제 -1 출력 이제 봄 하...
for i in range(N):
    for j in range(M):
        if visited[i][j] == -1:
            graph[i][j] = 0

# 위 아래 왼쪽 오른쪽
moves = [(0,-1), (0,1), (-1,0), (1, 0)]

# 시작 부분 찾기
for i in range(N):
    for j in range(M):
        if visited[i][j] == 1:
            # 그래프 작성
            BFS(i, j)
            # 출력        
            for k in range(N):
                print(*graph[k])
            exit()
                       
