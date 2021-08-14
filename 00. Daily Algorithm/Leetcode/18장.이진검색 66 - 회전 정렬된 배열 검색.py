# https://leetcode.com/problems/search-in-rotated-sorted-array
# 풀이 1 : 책과 조금 다른 풀이. 굳이 mid 찾을 필요 없음

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums: return -1
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[hi]:
                if target >= nums[mid] and target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1
            else:
                if target >= nums[lo] and target <= nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
        return -1

