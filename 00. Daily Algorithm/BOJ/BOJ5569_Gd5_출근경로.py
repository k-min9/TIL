'''
스터디 동료 풀이 리팩토링
핵심은 현재좌표, 방향전환가능 플래그를 가진 4차원 dp
'''
import sys
input = sys.stdin.readline

# 도로 개수 : 남북 w 동서 h
# 방향 전환 불가 : 0  / 가능 : 1
w, h = map(int,input().split())
dp = [[[[0 for _ in range(2)] for _ in range(2)] for _ in range(101)] for _ in range(101)]

for i in range(2,h+1):
    dp[i][1][0][0] = 1
for i in range(2,w+1):
    dp[1][i][0][1] = 1

for i in range(2,h+1):
    for j in range(2,w+1):
        dp[i][j][0][0] = (dp[i-1][j][0][0] + dp[i-1][j][1][0])%100000
        dp[i][j][0][1] = (dp[i][j-1][0][1] + dp[i][j-1][1][1])%100000
        dp[i][j][1][0] = (dp[i-1][j][0][1])%100000
        dp[i][j][1][1] = (dp[i][j-1][0][0])%100000

print((dp[h][w][0][0] + dp[h][w][1][0] + dp[h][w][0][1] + dp[h][w][1][1])%100000)