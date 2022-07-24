'''
그 가격까지의 합산 방식이 최소와 동일하면 플러스 아닐 경우 갱신...!
dp[x] : x원 지불을 위해 필요한 최소 동전갯수
'''
import sys
input = sys.stdin.readline

# 거꾸로 적으면 최소갯수가 그리디하게 나옴
COINS = [7, 5, 2, 1] 

N = int(input())
dp = [100001]*(N+1) 
dp[0] = 0


for m in range(1, N+1): 
    for coin in COINS:
        # 액면가보다 큼 & 기존 경우보다 개수를 줄일 수 있는 경우
        if coin <= m and dp[m-coin]+1 < dp[m]:
            dp[m] = dp[m-coin]+1

print(dp[-1])
