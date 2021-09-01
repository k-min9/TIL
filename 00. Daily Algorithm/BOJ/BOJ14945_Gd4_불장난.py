'''
DP 문제. 
불은 무시. 가로 이동 안되고 전진만 할 수 있다는 내용임
두 인간이 충돌하면 안 됨 >> 거리가 DP에 들어가야 되고 그 값이 0이면 안된다.
'''
import sys
input = sys.stdin.readline

N = int(input())
dp = [[0]*(N+1) for _ in range(N+1)]

# 현재 층, 두 인간의 거리
dp[2][1] = 2
for i in range(3,N+1):
    for j in range(1,i):
        # 거리 유지, 거리 + 1, 거리 - 1
        dp[i][j] = (dp[i-1][j]*2 + dp[i-1][j-1] + dp[i-1][j+1]) % 10007

print(sum(dp[N])%10007)