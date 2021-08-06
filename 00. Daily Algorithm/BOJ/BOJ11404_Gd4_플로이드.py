'''
레알 순도 100% 플로이드
'''

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = 1e9

maps = [[INF]*N for _ in range(N)]

for _ in range(M):
    a,b,c = map(int,input().split())
    maps[a-1][b-1]=min(maps[a-1][b-1],c)

for i in range(N):
    maps[i][i]=0

for k in range(N):
    for i in range(N):
        for j in range(N):
            maps[i][j] = min(maps[i][j], maps[i][k]+maps[k][j])

for i in range(N):
    for j in range(N):
        if maps[i][j] == INF:
            maps[i][j] = 0

for map in maps:
    print(*map)