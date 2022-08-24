'''
초심을 잃지 않고 느리게 푸는게 핵심이다
N = 100! 느리게!
'''
import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0
for a, b, c in combinations(cards, 3):
    if a+b+c<=M and M-(a+b+c) < M-answer:
        answer = a+b+c

print(answer)

'''
초심의! 소중함을! 지킬필요가 있었으니까!
'''