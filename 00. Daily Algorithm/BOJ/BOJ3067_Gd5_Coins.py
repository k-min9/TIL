'''
N가지 동전으로 M원을 만드는 가지수
'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    # dp[x] = x원을 만들 수 있는 가지 수
    dp = [0] * (M+1)
    dp[0] = 1
    for i in range(N):
        for j in range(coins[i], M+1):
            dp[j] += dp[j-coins[i]]
    
    print(dp[M])

'''
심플 이즈 베스트!
'''