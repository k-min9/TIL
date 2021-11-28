'''
dp로 해당금액을 만드는데 필요한 동전의 개수를 최소로 나타낸다면
dp[해당금액] = dp[해당금액 - 코인 종류] + 1 중 작은 것
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [0] * (K+1)

for i in range(1, K+1):
    a = []
    for coin in coins:
        if coin <= i and dp[i-coin] != -1:
            a.append(dp[i-coin])

    if not a:
        dp[i] = -1
    else:
        dp[i] = min(a) + 1

print(dp[K])
