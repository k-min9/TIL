# https://leetcode.com/problems/maximum-subarray
# 풀이  : 카데인 알고리즘

import sys

def maxSubArray(nums: list[int]) -> int:
    best = -sys.maxsize
    cur = 0
    for num in nums:
        # 변수를 두 개 써서 스타트지점 자동갱신
        cur = max(num, cur+num)  # 매몰비용 생각하니까 쉽네
        best = max(cur, best)
    return best

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))