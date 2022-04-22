'''
최소 힙을 절대값 힙으로 바꾸면 되는거지?
'''
import sys
input = sys.stdin.readline
import heapq

n = int(input())
q = []

for i in range(n):
    a = int(input().rstrip())
    if a != 0:
        # 튜플의 형태로 절대값과 원래값을 넣기
        heapq.heappush(q, (abs(a), a))
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
