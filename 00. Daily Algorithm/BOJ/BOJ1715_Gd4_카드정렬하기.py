from heapq import heappush, heappop
import sys

input = sys.stdin.readline

N = int(input())
cards = list()
for _ in range(N):
    heappush(cards, int(input()))

answer = 0
while len(cards) > 1:
    cost = heappop(cards) + heappop(cards)
    answer += cost
    heappush(cards, cost)
print(answer)