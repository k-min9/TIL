'''
dp[이동횟수][값]
'''
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    # 고르는 수, 최대 수
    n, m = map(int, input().split())

    # dp와 초기값
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[0] = [1]*(m+1)

    for x in range(1, n+1):
        for y in range(1, m+1):
            # y-1까지의 dp + 선택1회 적을때의 기존dp누적
            dp[x][y] = dp[x][y-1] + dp[x-1][y//2]
    
    print(dp[n][m])

    
'''
골드....4?
'''

