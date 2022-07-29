'''
메모장 열고 써보면
dp[i-2]+dp[i-3] = dp[i]
'''
import sys
input = sys.stdin.readline

dp = [0,1,1,1] + [0] * 100
for i in range(4, 101):
    dp[i] = dp[i-3] + dp[i-2]

for _ in range(int(input())):
    print(dp[int(input())])

'''
새로운 언어 공부... 중!
'''