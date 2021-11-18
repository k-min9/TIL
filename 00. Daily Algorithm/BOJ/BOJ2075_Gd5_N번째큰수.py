'''
우선순위 큐 문제
>>> 메모리 제한 문제 요점은 큐의 길이를 N으로 유지하는 것
'''
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    nums = list(map(int,input().split()))

    if not heap: 
        for num in nums:
            heappush(heap,num)
    else:
        for num in nums:
            if heap[0] < num:
                heappush(heap,num)
                heappop(heap)
    
print(heap[0])