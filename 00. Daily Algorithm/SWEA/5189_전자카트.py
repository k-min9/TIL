import sys
sys.stdin = open('input.txt')

# 상수
INF = sys.maxsize


def backtrack(current, visit):
    # 방문 종료
    if visit == (1 << N)-1:
        return dists[current][0]

    # 이미 방문
    if dp[current][visit] != INF:
        return dp[current][visit]

    for i in range(1, N):
        # 방문 안 함
        if not visit & (1 << i):
            dp[current][visit] = min(dp[current][visit], backtrack(i, visit|(1<<i)) + dists[current][i])

    return dp[current][visit]


for t in range(int(input())):
    N = int(input())
    dists = [list(map(int,input().split()))for _ in range(N)]
    dp = [[INF]*(1 << N)for _ in range(N)]

    print(f'#{t+1}', backtrack(0, 1))
