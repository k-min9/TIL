'''
dp[0~9 숫자등장상황(bit)][자리 수][마지막 수]

'''
import sys
input = sys.stdin.readline


# 상수
MOD = 1000000000


N = int(input())
# 3차원 리스트 생성
dp = [[[0]*10 for _ in range(N)] for _ in range(1024)]
# 초기 값
for i in range(1, 10):
    dp[1<<i][0][i] = 1

# DP 깔끔히
for i in range(1, N):
    for end in range(10):
        for bit in range(1024):
            if end < 9:
                dp[bit|(1<<end)][i][end] = (dp[bit|(1<<end)][i][end] + dp[bit][i-1][end+1]) % MOD
            if end > 0:
                dp[bit|(1<<end)][i][end] = (dp[bit|(1<<end)][i][end] + dp[bit][i-1][end-1]) % MOD

print(sum(dp[1023][N-1]) % MOD)