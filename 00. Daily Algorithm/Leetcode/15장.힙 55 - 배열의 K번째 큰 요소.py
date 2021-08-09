# https://leetcode.com/problems/kth-largest-element-in-an-array
# 풀이 1 : 최대 heap 만들어보자.

import heapq

def findKthLargest(self, nums: list[int], k: int) -> int:
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n)
        
    for _ in range(1, k):
        heapq.heappop(heap)
        
    return -heapq.heappop(heap)

'''
풀이 2 : heapq 모듈의 heapify 이용
풀이 3 : heapq 모듈의 nlargest 이용
'''