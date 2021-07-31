# https://leetcode.com/problems/two-sum/
# 풀이 4: 조회구조 개선

def twoSum(nums: list[int], target: int) -> list[int]:
    nums_map = {}
    # 하나의 for문으로 제어
    for i, num in enumerate(nums):
        if target - num in nums_map:
             return [nums_map[target - num], i]
        nums_map[num] = i
        print(nums_map)

print(twoSum([2, 7, 11, 15], 26))