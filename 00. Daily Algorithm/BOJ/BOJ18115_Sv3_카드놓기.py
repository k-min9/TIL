'''
deque를 실제로 만들어 보기 같은 느낌인데...
역으로 넣는게 포인트
'''
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
cards = list(map(int, input().split()))

result = deque()

for i in range(N):
    if cards[N-i-1] == 1:
        result.appendleft(i+1)
    elif cards[N-i-1] == 2:
        result.insert(1,i+1)
    elif cards[N-i-1] == 3:
        result.append(i+1)

print(*result)
