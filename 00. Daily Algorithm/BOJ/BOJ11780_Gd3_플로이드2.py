'''
플로이드1(BOJ11404) 
+ 경로(https://hooongs.tistory.com/325)
'''

import sys
input = sys.stdin.readline

# 확실히 경로째 리스트로 담는것보다 이쪽이 메모리가 작겠지
def find_path(i, j):
    if paths[i][j] == 0:
        return []

    k = paths[i][j]
    text = find_path(i,k) + [k] + find_path(k, j)
    return text 

N = int(input())
M = int(input())
INF = 1e9

# 인풋
maps = [[INF]*(N+1) for _ in range(N+1)]
paths = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    maps[a][b]=min(maps[a][b],c)

for i in range(N+1):
    maps[i][i]=0

# 플로이드
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1, N+1):
            if maps[i][j] > maps[i][k] + maps[k][j]:
                maps[i][j] = maps[i][k] + maps[k][j]
                paths[i][j] = k  # 기록

for i in range(1,N+1):
    for j in range(1, N+1):
        if maps[i][j] == INF:
            maps[i][j] = 0

# 출력
for i, map in enumerate(maps):
    if i!=0: 
        print(*map[1:])

for i in range(1,N+1):
    for j in range(1,N+1):
        if maps[i][j] == 0:
            print(0)
            continue
        path = [i] + find_path(i,j) + [j]
        print(len(path), end=' ')
        print(*path)

'''
플로이드는 어차피 용량이나 최적화 버린거 N+1로 구축하는게 머리 인식이 빠르다는걸 깨달음 
물론 N도 가능함 중간중간 마이너스 넣다가 실제 시험장이나 다시 구축할때 절대로 이 방법으로 안할거 같아서 N+1로 재구축
'''