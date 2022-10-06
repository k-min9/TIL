'''
플로이드 연습
'''
import sys
input = sys.stdin.readline

INF = sys.maxsize

N, M = map(int,input().split())
graphs = [[INF]*N for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    a-=1
    b-=1
    graphs[a][b] = 1
    graphs[b][a] = 1

# 플로이드-와샬
for k in range(N):
    graphs[k][k] = 0  # 자기 자신 = 관계 0
    for i in range(N):
        for j in range(N):
            graphs[i][j] = min(graphs[i][j], graphs[i][k] + graphs[k][j])

kebin = INF
answer = 0
for i in range(N):
    tmp = sum(graphs[i])
    if kebin > tmp:
        kebin = tmp
        answer = i

print(answer+1)
