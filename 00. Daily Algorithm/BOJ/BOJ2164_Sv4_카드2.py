'''
이거 왠지 수학문제 삘 나는데...
'''
from collections import deque

n = int(input())
cards = deque(range(1,n+1))
answer = n
while cards:
    answer = cards.popleft()
    if cards:
        cards.append(cards.popleft())
print(answer)