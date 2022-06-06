'''
DP로 쭉 계산하면서 올라가면 끝인거 같음
'''
import sys
input = sys.stdin.readline

INF = 987654321


N = int(input())
cards = [0] + list(map(int, input().split()))
dp = [INF] * (N+1)
dp[0] = 0

for i in range(1, N+1):
    for k in range(1, i+1):
        dp[i] = min(dp[i], dp[i-k] + cards[k])

print(dp[N])
