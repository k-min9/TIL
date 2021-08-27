'''
LIS 잖아...
'''

import sys
input = sys.stdin.readline

from bisect import bisect_left #내부 함수, 이진탐색의 시간복잡도는 O(logN)이다. bisect_left는 lowerbound

def getDP_LIS(seq):
    A = [0] #상수는 아니지만 이해를 위해 예시대로 대문자로 간다.

    for x in seq:
        if A[-1]<x: #마지막 숫자 비교
            A.append(x) # 추가
        else:
            A[bisect_left(A,x)]=x #갱신

    return A


# 입력
N = int(input()) # 수열 크기
seq = list(map(int,input().split()))[::-1] #수열

#출력
print(N-len(getDP_LIS(seq))+1)