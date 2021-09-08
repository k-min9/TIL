'''
itertool 쓰는 이유는 생산성과 C라이브러리!
절대 귀찮아서가 아님!
'''
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
k = int(input())
cards = [input().rstrip() for _ in range(n)]

answers = set()
for p in permutations(cards, k):
    answers.add(''.join(p))

print(len(answers))
