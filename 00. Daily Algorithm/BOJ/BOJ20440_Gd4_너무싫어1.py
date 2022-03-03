'''
모기 + 회의실 문제인거 같은데...
모기가 가장 많을때와 시간대
'''
import sys
input = sys.stdin.readline
from heapq import heappop, heappush


answer_cnt = 0
answer_range = [0, 0]
mosquitos = [tuple(map(int, input().split())) for _ in range(int(input()))]
mosquitos.sort()

heap = []

for s, e in mosquitos:
    if heap and heap[0][0] <= s:
        heappop(heap)
    
    heappush(heap, (e, s))
    
    if len(heap) == answer_cnt and answer_range[1] == s:
        answer_range[1] = heap[0][0]
    elif len(heap) > answer_cnt:
        answer_cnt = len(heap)
        answer_range = [s, heap[0][0]]

print(answer_cnt)
print(answer_range[0], answer_range[1])

'''
회의실 = heap + s + e : 수고하셨습니다.
'''