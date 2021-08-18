# https://leetcode.com/problems/majority-element
# 풀이 3 : 분할 정복

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        mid = len(nums) // 2
        
        a = self.majorityElement(nums[:mid])
        b = self.majorityElement(nums[mid:])

        return [b, a][nums.count(a) > mid]



# 카운터, 배열해서 정리도 끝
