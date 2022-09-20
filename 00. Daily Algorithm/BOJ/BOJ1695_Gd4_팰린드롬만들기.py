'''
DP + 팰린드롬
수열과 역순수열의 최장 공통 수열을 찾은 후 N에서 빼면 된다.
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        if nums[-i]==nums[j-1] : 
            dp[i][j] = dp[i-1][j-1]+1
        else : dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(N-dp[N][N])
