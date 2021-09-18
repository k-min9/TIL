'''
아침을 여는 문제!
'''

import sys
from math import ceil
input = sys.stdin.readline

end = int(input())
M = int(input())
x = list(map(int, input().split()))

answer = max(x[0]-0, end-x[-1])
for i in range(M-1):
    answer = max(answer, ceil((x[i+1]-x[i])/2))
print(answer)