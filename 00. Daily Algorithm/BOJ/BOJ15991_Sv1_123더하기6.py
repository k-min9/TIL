'''
중앙을 기점으로 0,1,2,3으로 두고 남은건 왼팔 오른팔 붙이면 끝인거 같은데
'''
import sys
input = sys.stdin.readline

MOD = 1000000009

dp = [0] * 50001
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4

# 바텀 업
for i in range(4,50001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD

# 종료
N = int(input())
for _ in range(N):
    i = int(input())
    # 초기값
    if i == 1:
        answer = 1
    elif i == 2:
        answer = 2

    # 총합이 짝수
    elif i%2 == 0:
        answer = (dp[i//2] + dp[(i-2)//2]) % MOD
    else:
        answer = (dp[(i-1)//2] + dp[(i-3)//2]) % MOD
    print(answer)