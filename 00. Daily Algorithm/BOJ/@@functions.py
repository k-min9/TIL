# git의 함수찾기 기능을 이용한 함수 모음집

def dfs():
    pass

def floid(maps, i, j, k):
    # 경유지, 목적지, 기본 이동 코스
    for k in range(26):
        for i in range(26):
            for j in range(26):
                if maps[i][j] > maps[i][k] + maps[k][j]:
                    maps[i][j] = maps[i][k] + maps[k][j]

def dijkstra(nodeStart):
    pass

def union():
    pass

dijkstra(1)
dfs()
floid()
union()