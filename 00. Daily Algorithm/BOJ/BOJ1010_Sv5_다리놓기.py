'''
접근 : 와 mCn이다!
'''
import sys
input = sys.stdin.readline
from math import factorial

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(factorial(b)//factorial(a)//factorial(b-a))


'''
저어는 이게 조합 모든 경우의 수를 다 뽑을 줄 몰랐어요
from itertools import combinations
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(len(list(combinations(range(max(a,b)),min(a,b)))))
'''