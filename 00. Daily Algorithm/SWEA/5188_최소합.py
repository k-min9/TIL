import sys
sys.stdin = open('input.txt')

for t in range(int(input())):
    # 가로, 세로 칸 수
    N = int(input())
    dp = [list(map(int, input().split())) for _ in range(N)]

    for x in range(1, N):
        dp[x][0] += dp[x-1][0]
    for y in range(1, N):
        dp[0][y] += dp[0][y-1]

    for x in range(1, N):
        for y in range(1, N):
            dp[x][y] = dp[x][y] + min(dp[x-1][y], dp[x][y-1])

    print(f'#{t+1}', dp[N-1][N-1])
