'''
DP지? DP네
요지는 어느 시점의 dp를 가져오느냐 이기 때문에 생각보다 단순하게 처리할 수 있다.
'''
import sys
input = sys.stdin.readline

N = int(input())
wine = [int(input()) for _ in range(N)]

dp = [0]*(N+1)
dp[1] = wine[0]
if N > 1:
    dp[2] = wine[0] + wine[1]

for i in range(3, N+1):
    # 마시지 않는다. 마시는데, 전단계꺼를 안마셨을뿐이다. 전전단계꺼를 안마셨을뿐이다.
    dp[i] = max(dp[i-1], wine[i-1] + dp[i-2], wine[i-1] + wine[i-2] + dp[i-3])
    
print(dp[N])
