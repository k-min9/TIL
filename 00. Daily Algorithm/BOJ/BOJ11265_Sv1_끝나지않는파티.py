'''
읽는 중간까지 최소 스패닝트리인줄 알았음. 네비게이션이라니 누가 알았단 말인가.
'''

import sys
input = sys.stdin.readline

INF = 1e9
N, M = map(int, input().split())

# 인풋
#maps = [[INF]*500 for _ in range(500)]
maps = list()
for _ in range(N):
    maps.append(list(map(int, input().split())))

# 플로이드
for k in range(N):
    for i in range(N):
        for j in range(N):
            if maps[i][j] > maps[i][k] + maps[k][j]:
                maps[i][j] = maps[i][k] + maps[k][j]

# for m in maps:
#     print(*m)

# 출력 (손님들)
for _ in range(M):
    start, end, t = map(int, input().split())
    if maps[start-1][end-1] > t:
        print('Stay here')
    else:
        print('Enjoy other party')