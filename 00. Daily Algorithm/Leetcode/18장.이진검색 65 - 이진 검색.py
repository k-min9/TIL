# https://leetcode.com/problems/binary-search
# 풀이 2 : 이진검색 구현

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l=0
        r=len(nums)
        while(l<r):
            # 오버플로 막기
            mid=l+(r-l)//2 
            # print(m)
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                l=mid+1
            else:
                r=mid
        return -1