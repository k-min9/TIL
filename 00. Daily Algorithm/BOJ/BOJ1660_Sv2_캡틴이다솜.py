'''
DP로 쭉 적고 출력하면 끝
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list()

# 1차 삼각형
num = 0
idx = 1
while num < N:
    num += (idx * (idx + 1)) // 2
    nums.append(num)
    idx += 1

# DP로 사면체 작성
dp = [float('inf')] * (N + 1)
for i in range(1, N + 1):
    for num in nums:
        if num == i:
            dp[i] = 1
            break
        if num > i: break
        dp[i] = min(dp[i], 1 + dp[i - num])

# 출력
print(dp[N])
