'''
visit - 11010 : 2번 4번 5번 방문
'''
import sys
input = sys.stdin.readline

# 상수
INF = sys.maxsize


def backtrack(current, visit):
    # 방문 종료
    if visit == (1<<N)-1:
        if dists[current][0] == 0:
            return INF
        else:
            return dists[current][0]

    # 이미 방문
    if dp[current][visit]!=INF:
        return dp[current][visit]

    for i in range(1,N):
        # 방문 안 함 + 방문할 수 있음
        if not visit&(1<<i) and dists[current][i]!=0:
            dp[current][visit] = min(dp[current][visit], backtrack(i, visit|(1<<i)) + dists[current][i])

    return dp[current][visit]

N = int(input())
dists = [list(map(int,input().split()))for _ in range(N)]
dp=[[INF]*(1<<N)for _ in range(N)]

print(backtrack(0,1))