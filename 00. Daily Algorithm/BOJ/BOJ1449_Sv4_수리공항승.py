import sys
input = sys.stdin.readline

# 물이 새는 곳, 테이프 길이
N, L = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

answer = 0
now = 0
for num in nums:
    if num <= now:
        continue
    else:
        answer += 1
        now = num + L - 1

print(answer)
