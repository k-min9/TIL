'''
디ㅡ피ㅡ
'''

import sys
input = sys.stdin.readline

# 솔직히 N이 너무 적어서 안써도 될거 같은데
dp = [0] * 10
dp[0] = 1
dp[1] = 2
dp[2] = 4

# 바텀 업
for i in range(7):
    dp[i+3] = dp[i+2] + dp[i+1] + dp[i]

# 종료
N = int(input())
for _ in range(N):
    print(dp[int(input())-1])