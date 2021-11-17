'''
1
01
1001
01101001
반으로 나누면 뒤집힌 전단계 + 전단계 임 (01101001 = 0110 + 1001)
dp(N) = dp(N-1)*2 + 1 / -1 (N번째, N-1번째)
'''
import sys
input = sys.stdin.readline

N=int(input())
dp=[0, 0, 1]
for i in range(3, N+1):
    if i%2==0: dp.append(dp[i-1]*2+1)
    else: dp.append(dp[i-1]*2-1)
print(dp[N])