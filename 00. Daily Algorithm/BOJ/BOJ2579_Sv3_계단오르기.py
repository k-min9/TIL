'''
DP 연습용
'''
import sys
input = sys.stdin.readline

# 입력
N = int(input())
stairs = [0]+[int(input()) for _ in range(N)]

if N == 1:
    print(stairs[1])
else:
    dp = [0] * (N+1)
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2] 

    for i in range(3, N+1):
        # 전 계단을 밟았으면 그 전에는 무조건 밟으면 안되고 / 안 밟았으면 두 단계 전을 밟고 올라왔을테고. 완벽히 양분화
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])  

    print(dp[N])