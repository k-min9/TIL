'''
C를 달성하기 위한 최소 금액
'''
import sys
input = sys.stdin.readline

C, N = map(int, input().split())
ads = [list(map(int, input().split())) for _ in range(N)]
dp = [0] + [sys.maxsize] * (C+100)  # 한번에 100미만

for cost, customer in ads:
    for i in range(customer, C+101):
        dp[i] = min(dp[i], dp[i - customer] + cost)

print(min(dp[C:]))
