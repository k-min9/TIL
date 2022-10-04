'''
deque로 하나도 안남고 빌때까지 뺑뺑이...
'''
from collections import deque
import sys

n, k = map(int, input().split())
queue = deque(range(1, n+1))

print('<', end='')
while queue:
    for i in range(k - 1):
        queue.append(queue[0])
        queue.popleft()
    print(queue.popleft(), end='')
    if queue:
        print(', ', end='')
print('>')
