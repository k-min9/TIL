'''
DP 강화 기간인가?
그거만 파악하면 그 다음은 메모장에 적고 점화식 찾는 수학 문제에 가까움
'''
import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+2)]
dp[0] = 1
dp[1] = 2
dp[2] = 7

for i in range(3, N+1):
    dp[i]=(dp[i-1]*3+dp[i-2]-dp[i-3])%1000000007

print(dp[N]%1000000007)
