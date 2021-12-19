'''
x1x2 + x1x3 + ... xn-1xn = x1(x2+...+xn) + x2(x3+...+xn) + ... xn-1xn
즉 누적합을 쓰면 O(N)
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
sums = list()
sums.append(nums[0])

for i in range(1, N):
    sums.append(sums[i-1] + nums[i])

answer = 0
for i in range(N):
    answer += nums[i] * (sums[N-1] - sums[i])

print(answer)