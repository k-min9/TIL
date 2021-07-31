# https://leetcode.com/problems/array-partition-i
# 풀이 3: 내가 푼 줄 알았는데 있었다.

def arrayPairSum(self, nums: list[int]) -> int:
    nums.sort()
    
    return sum(nums[::2])