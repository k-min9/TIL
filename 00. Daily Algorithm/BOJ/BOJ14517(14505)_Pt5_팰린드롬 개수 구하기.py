'''
# from : https://www.crocus.co.kr/869
'''

import sys
input = sys.stdin.readline

s = input().rstrip()
n = len(s)
dp = [[0 for _ in range(1005)] for _ in range(1005)]

for i in range(n):
    # 한 글자 (a)
    dp[i][i] = 1

    if i != n-1:
        # aa -> a, a, aa
        if s[i] == s[i+1]:
            dp[i][i+1] = 3

        # ab -> a, b
        else:
            dp[i][i+1] = 2

for i in range(n):
    for left in range(n):
        right = left + i

        if right >= n:
            break

        dp[left][right] = dp[left+1][right] + dp[left][right-1]-dp[left+1][right-1]

        if s[left] == s[right]:
            dp[left][right] += dp[left+1][right-1]+1

print(dp[0][n-1]%10007)