'''
N 종류의 동전을 적당히 써서 그 가치의 합이 K원이 되도록 하는 경우의 수
배낭식으로 2차원 DP
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

dp = [0]*(K+1)
dp[0] = 1

for num in nums:
    for j in range(1, K+1):
        if j - num >= 0:
            dp[j] += dp[j-num]

print(dp[K])
