# https://leetcode.com/problems/single-number
# 풀이  : XOR 풀이

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
            
        return result