'''
4개를 합쳐서 그 합의 최대값. => ㅗ 모양 말고, 길이 4인 dfs
견적 : 
범위 : 1000 * 1000 = 100만
제한시간 2초 -> 4천만
브루탈하게 가도 되겠는데??
'''
import sys
input = sys.stdin.readline

#상수
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 기본적인 테트로미노
def dfs(x, y, length, sums):
    if length == 4:
        global answer
        answer = max(answer, sums)
        return
    
    for dx, dy in MOVES:
        nx, ny = x+dx, y+dy
        if 0<=ny<N and 0<=nx<M and not visited[ny][nx]:
            visited[ny][nx] = 1
            dfs(nx, ny, length+1, sums + graphs[ny][nx])
            visited[ny][nx] = 0

# 특수 테트로미노 ㅗ
def calc(x, y):
    temp = list()
    for dx, dy in MOVES:
        nx, ny = x+dx, y+dy
        if 0<=ny<N and 0<=nx<M:
            temp.append(graphs[ny][nx])
    if len(temp)>=3:
        global answer
        result = graphs[y][x] + sum(sorted(temp, reverse=True)[:3])
        answer = max(answer, result)
    

# 세로, 가로
N, M = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(N)]

# 계산
answer = 0 
visited = [[0]*M for _ in range(N)]
for y in range(N):
    for x in range(M):
        visited[y][x]=1
        dfs(x, y, 1, graphs[y][x])
        visited[y][x]=0
        calc(x, y)

print(answer)
