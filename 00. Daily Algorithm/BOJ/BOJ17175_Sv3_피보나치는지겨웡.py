'''
dp문제의 dp...
f(5) = f(4) + f(3)이니까 dp횟수는 dp[5] = dp[4] + dp[3] + 1이 될테고 반복
'''
import sys
input = sys.stdin.readline

# 상수
MOD = 1000000007

# DP
dp = [0]*51
dp[0] = 1
dp[1] = 1
for i in range(2, 51):
    dp[i] = (dp[i-1] + dp[i-2] + 1) % MOD

# 출력
print(dp[int(input())])