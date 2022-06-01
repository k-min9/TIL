'''
이론문제
연결되있는 선이 1개보다 많으면 단절점
싸이클이 없는 트리이기 때문에 모든 간선이 단절선이 된다.
'''
import sys
input = sys.stdin.readline
 
# 간선
N = int(input())
info = [0]*(N+1)
for _ in range(N-1):
    s, e = map(int, input().split())
    info[s] += 1
    info[e] += 1
 
# 쿼리
M = int(input())
for _ in range(M):
    flag = False
    q, v = map(int, input().split())
    if q == 1:
        if info[v] > 1:
            flag = True
    else:
        flag = True
 
    if flag:
        print("yes")
    else:
        print("no")

