'''
아홉 중에 일곱의 합이 100인 수열
'''
import sys
input = sys.stdin.readline


def solve():
    for i in range(8):
        for j in range(i+1, 9):
            if sums - nums[i] - nums[j] == 100:
                return {nums[i], nums[j]}


nums = [int(input()) for _ in range(9)]
sums = sum(nums)
sets = solve()
nums.sort()
for num in nums:
    if num not in sets:
        print(num)
