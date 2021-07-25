# 기본 전처리
import sys
input = sys.stdin.readline

#힙
from heapq import heappop, heappush
heapExample = []
heappush(heapExample,[100,10])
print('heap', heapExample)
heappush(heapExample,[70,20])
print('heap', heapExample)
heappush(heapExample,[90,30])
print('heap', heapExample)
heappush(heapExample,[80,30])
print('heap', heapExample)
heappop(heapExample)
print('heap', heapExample)
heappop(heapExample)
print('heap', heapExample)

#덱
from collections import deque
q = deque()
q.append([100,10])
print('q', q)
q.append([70,20])
print('q', q)
q.append([90,30])
print('q', q)
q.popleft() # 리턴으로 볼 수 있음
print('q', q)
q.append([80,30])
print('q', q)

# 시간 재기 (간략)
import time
t0 = time.time()
print("시간:", time.time()-t0)

# 시간 재기 (정확)
import timeit
t0 = timeit.default_timer()
print("시간:", timeit.default_timer()-t0)