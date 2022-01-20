'''
N개의 물건이 각각 W와 V의 가치 최대 K 무게 => 가장 최댓값
0-1 냅색 문제네
해당 무게까지의 DP로 가치 계산하면 뭐...
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0]*(K+1)

for _ in range(N):
    W, V = map(int, input().split())
    for i in range(K, W-1, -1):
        dp[i] = max(dp[i], dp[i-W] + V)

print(dp[K])
