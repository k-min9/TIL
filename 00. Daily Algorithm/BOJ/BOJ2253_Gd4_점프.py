'''
dp[현재속도][현재위치] = min(dp[현재속도-1][현재위치-현재속도], dp[현재속도][현재위치-현재속도], dp[현재속도+1][현재위치-현재속도]) + 1
10000이니까 최대속도는 N*(N+1)/2 > 10000 즉 N은 대충 150보다 크거나 작다
현재속도랑 위치 뒤집는게 나중에 answer 뽑기 편함
'''
import sys
input = sys.stdin.readline

# 상수
INF = 300

# 초기화
N, M = map(int, input().split())

dp = [[INF]*(150) for _ in range(N+1)]
dp[1][0] = 0

stop = set(int(input()) for _ in range(M))

# dp 시작
for x in range(2, N+1):
    if x in stop:
        continue
    for v in range(1, 149):
        if x > v:
            dp[x][v] = min(dp[x-v][v-1], dp[x-v][v], dp[x-v][v+1]) + 1

answer = min(dp[N])
if answer == INF:
    answer = -1
print(answer)