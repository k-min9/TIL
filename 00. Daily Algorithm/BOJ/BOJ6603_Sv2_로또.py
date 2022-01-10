'''
문제 보는 순간 그냥
파이썬이 사기인 이유 중 하나 itertools
네
'''
import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    else:
        nums = nums[1:]
    
    for comb in combinations(nums, 6):
        print(*comb)
    print()

