'''
DP? 최소힙 아니고?
'''

import sys
from heapq import heappop, heappush, heapify

T = int(input())
for _ in range(T):
    N = int(input())
    cases = list(map(int, input().split()))
    heapify(cases)
    answer = 0
    for _ in range(N-1):
        n = heappop(cases) + heappop(cases)
        heappush(cases, n)
        answer = answer + n
        print('a', n,':',answer, cases)
    print(answer)
    
'''
아니네, 나중에 시간 나면 DP 하는 걸로
'''