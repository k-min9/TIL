import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, *battery = map(int, input().split())
    dp = [10001] * N
    dp[N-1] = 0

    for i in range(N - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if j + battery[j] >= i:
                dp[j] = min(dp[j], dp[i] + 1)

    print(f'#{tc+1}', dp[0]-1)
