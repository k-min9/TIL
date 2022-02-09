'''
가즈아
'''
import sys
input = sys.stdin.readline

answer = 0
nums = input().strip()
if len(nums) == 1:
    nums = '0' + nums

start = nums
while True:
    answer += 1
    tmp = str(int(nums[0])+ int(nums[1]))
    nums = nums[1] + tmp[-1]
    if nums == start:
        break
print(answer)
