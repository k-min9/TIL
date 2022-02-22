'''
DP로 한번 해보고...
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [987654321]*1200
dp[0] = 0

for i in range(N):
    for j in range(nums[i]+1):
        dp[i+j] = min(dp[i+j], dp[i]+1)
    
answer = dp[N-1]
if answer == 987654321:
    answer = -1
print(answer)
