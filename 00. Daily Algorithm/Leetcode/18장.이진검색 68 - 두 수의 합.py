# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
# 풀이 5 : 노 슬라이스 + 이진 검색

import bisect

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k + 1)
            if i < len(numbers) and numbers[i] == expected:
                return k+1, i+1