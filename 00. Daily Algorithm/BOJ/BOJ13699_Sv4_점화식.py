'''
D~P~
'''
import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*36
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    t = 0
    if i%2:
        for j in range(i//2):
            t += 2*dp[j]*dp[i-j-1]
        dp[i] = t + dp[i//2]**2
    else:
        for j in range(i//2):
            t += 2*dp[j]*dp[i-j-1]
        dp[i] = t

print(dp[N])
