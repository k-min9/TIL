'''
d~ p~
[y][x][도착시 파이프방향]
0 : 가로 , 1 : 세로, 2: 대각선
'''

import sys
input = sys.stdin.readline

N = int(input())
walls = [[0]*(N+1)]
for i in range(N):
    walls.append([0]+list(map(int, input().split())))

dp = [[[0]*3 for _ in range(N+1)] for _ in range(N+1)]
dp[1][2][0] = 1

for y in range(1, N+1):
    for x in range(1, N+1):
        if walls[y][x] == 0:
            dp[y][x][0] += dp[y][x-1][0] + dp[y][x-1][2] # dp[1][2][0] 안지워지게 얘만 +=
            dp[y][x][1] = dp[y-1][x][1] + dp[y-1][x][2]
            if walls[y-1][x] == 0 and walls[y][x-1] == 0:
                dp[y][x][2] = dp[y-1][x-1][0] + dp[y-1][x-1][1] + dp[y-1][x-1][2]

print(dp[y][x][0] + dp[y][x][1] + dp[y][x][2])

'''
같은 문제 를 두개 올리는거 생각보다 많긴 한데 아예 이름까지 같은 채로 번호 하나차이에 이름도 1, 2 구분된건 처음인거 같은 기분이;;
'''