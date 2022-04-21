'''
알고리즘 처음 풀때의 초심으로
DP
'''
import sys
input = sys.stdin.readline

words1 = input().rstrip()
words2 = input().rstrip()

M = len(words1)
N = len(words2)
dp = [[0] * (N + 1) for _ in range(M + 1)]

for i in range(M):
    for j in range(N):
        if words1[i] == words2[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

print(dp[M][N])

'''
원래 2중 포문 맞던가...?
'''