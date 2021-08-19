# https://leetcode.com/problems/house-robber
# 풀이  : 기본 DP로 푸느니 카데인2

class Solution():
    def rob(self, nums):
        prev_max = 0
        curr_max = 0
        for num in nums:
            prev_max, curr_max = curr_max, max(prev_max + num, curr_max)
        return curr_max

"""
정식 DP
if nums is None or len(nums) == 0:
    return 0
if len(nums) == 1:
    return nums[0]


dp = [nums[0], max(nums[0], nums[1])]

for i in range(2, len(nums)):
    dp.append(max(dp[i -2] + nums[i], dp[i - 1]))

return dp[-1]
"""