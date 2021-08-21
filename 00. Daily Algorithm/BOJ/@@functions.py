# git의 함수찾기 기능을 이용한 함수 모음집

def dfs():
    pass

def bfs():
    pass

def dijkstra(nodeStart):
    pass

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


dfs()
bfs()
dijkstra(1)
floid()
union()
divide()