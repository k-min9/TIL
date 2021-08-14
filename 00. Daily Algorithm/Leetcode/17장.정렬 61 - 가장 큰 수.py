# https://leetcode.com/problems/largest-number
# 풀이 X : 3.0에서 사라진 cmp를 functools 모듈을 써서 구현한 예시를 구경

from functools import cmp_to_key

class Solution:        
    def largestNumber(self, nums):
        
        def cmp_func(x, y):
            """Sorted by value of concatenated string increasingly."""
            if x + y > y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1
            
        # Build nums contains all numbers in the String format.
        nums = [str(num) for num in nums]
        
        # Sort nums by cmp_func decreasingly.
        nums.sort(key = cmp_to_key(cmp_func), reverse = True)
        
        # Remove leading 0s, if empty return '0'.
        return ''.join(nums).lstrip('0') or '0'

