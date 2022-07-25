'''
이미 있단 말이지 이거...
'''
import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())

answers = sorted(list(permutations(range(1, N+1), N)))
for answer in answers:
    print(*answer)
