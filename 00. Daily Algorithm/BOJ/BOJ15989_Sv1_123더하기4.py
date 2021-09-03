'''
2
11
2

3
111
21
3

4
1111
211
22
31

5
11111
2111
221
311
32

dp[n][가장큰숫자] = dp[n-3] + dp[n-2][1로끝남][2로끝남] +dp[n-1][1로 끝남]
>>
dp[n][3] = dp[n-3][1] + dp[n-3][2] + dp[n-3][3]
dp[n][2] = dp[n-2][1] + dp[n-1][2]
dp[n][1] = dp[n-1][1]
'''

import sys
input = sys.stdin.readline

dp = [[0]* 4 for _ in range(10001)]
dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

# 바텀 업
for n in range(4,10001):
    dp[n][3] = dp[n-3][1] + dp[n-3][2] + dp[n-3][3]
    dp[n][2] = dp[n-2][1] + dp[n-2][2]
    dp[n][1] = 1

# 종료
T = int(input())
for _ in range(T):
    print(sum(dp[int(input())]))