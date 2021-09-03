'''
[현재수][0 = 짝수, 1 = 홀수]
'''
import sys
input = sys.stdin.readline

#상수
MOD = 1000000009

dp = [[0]*2 for _ in range(100001)]

dp[1][1] = 1
dp[2][0] = 1
dp[2][1] = 1
dp[3][0] = 2
dp[3][1] = 2

# DP
for n in range(4,100001):
    dp[n][1] = (dp[n-1][0] + dp[n-2][0] + dp[n-3][0])%MOD
    dp[n][0] = (dp[n-1][1] + dp[n-2][1] + dp[n-3][1])%MOD

# 출력
T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N][1], dp[N][0])