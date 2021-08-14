# https://leetcode.com/problems/intersection-of-two-arrays
# 풀이 X : 아니 set 쓰라고

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        answers = set()
        
        for n in nums1:
            if n in nums2:
                answers.add(n)
        answers = list(answers)
        
        return answers

