'''
우측에서 찾은걸 쭉 적기만 하면 답인데...?
'''
import sys
input = sys.stdin.readline
from bisect import bisect_right

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answers = []
for idx, a in enumerate(A):
    answers.append(bisect_right(B, a) - idx - 1)
    
print(*answers)
