# git의 함수찾기 기능을 이용한 함수 모음집

def dfs():
    pass

def bfs():
    pass

def backtrack():
    # 종류 : dfs
    # 추천 문제 : 1248 맞춰봐, N-Queen
    pass

def dijkstra(nodeStart):
    pass

def bellmanFord(N, graph, dp, INF):
    global isPossible
    
    for repeat in range(N):
        for i in range(1, N + 1):
            for next, dist in graph[i]:
                if dp[i] != INF and dp[next] > dp[i] + dist:
                    dp[next] = dp[i] + dist
                    # 음의 싸이클 체크 = N-1바퀴 돌아도 갱신중
                    if repeat == N - 1:
                        isPossible = False

def floid(maps, i, j, k):
    # 경유지, 목적지, 기본 이동 코스
    for k in range(26):
        for i in range(26):
            for j in range(26):
                if maps[i][j] > maps[i][k] + maps[k][j]:
                    maps[i][j] = maps[i][k] + maps[k][j]

def union():
    pass

def divide():
    pass

def my_bisect():
    pass

def tarjan():
    # 종류 : CSS
    # 추천 문제 : 4013 도미노
    pass


dfs()
bfs()
backtrack()
dijkstra(1)
bellmanFord()
floid()
union()
divide()
my_bisect()
tarjan() # SCC 찾기용