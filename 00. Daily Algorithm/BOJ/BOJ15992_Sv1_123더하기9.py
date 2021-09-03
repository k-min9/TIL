'''
[현재수][사용한 숫자 수]
'''
import sys
input = sys.stdin.readline

#상수
MOD = 1000000009

dp = [[0]*1001 for _ in range(1001)]
dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 2
dp[3][3] = 1

# DP
for n in range(4,1001):
    for m in range(2,1001):
        dp[n][m] = (dp[n-1][m-1] + dp[n-2][m-1] + dp[n-3][m-1])%MOD

# 출력
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(sum(dp[N][:M+1])%MOD)