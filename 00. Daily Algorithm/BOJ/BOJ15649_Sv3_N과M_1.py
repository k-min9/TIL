'''
1~N까지 중복 없이 M개를 고른 수열
'''
import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(range(1,N+1))
for i in permutations(nums, M): 
    print(*i)
