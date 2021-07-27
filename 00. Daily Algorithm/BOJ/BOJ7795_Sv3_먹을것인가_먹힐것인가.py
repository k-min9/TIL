'''
이진탐색, 좌측에서, +1
ㄱㄱ!
'''

# 기본 전처리
import sys
input = sys.stdin.readline

from bisect import bisect_left

T = int(input())
for _ in range(T):
    numA, numB = map(int, input().split()) # 안 씀
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    b.sort()

    answer = 0
    for x in a:
        answer = answer + bisect_left(b, x)
    print(answer)
    
'''
+1 아니잖아!
'''
