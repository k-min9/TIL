# https://leetcode.com/problems/sliding-window-maximum
# 풀이 2 : 큐 + 슬라이딩 윈도우 O(N)

from collections import deque

def maxSlidingWindow(nums, k):
    d = deque()
    out = []
    for i, n in enumerate(nums):
        while d and nums[d[-1]] < n:
            d.pop()
        d += i,
        if d[0] == i - k:
            d.popleft()
        if i >= k - 1:
            out += nums[d[0]],
    return out

maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)

# 책 버전은 아니다. 직관성이 떨어지지만 재밌는 짧은 코드