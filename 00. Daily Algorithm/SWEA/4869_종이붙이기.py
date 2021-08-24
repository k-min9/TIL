import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    N = N//10
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 3
    for i in range(3, N+1):
        dp[i] = dp[i-1] + 2*dp[i-2]

    print(f'#{t+1}', dp[-1])
