'''
<가장 긴 증가하는 부분 수열(Longest Increasing Subsequence aka.LIS) 축제>
~ on 2021.07.24 from BOJ11053_Sv2_LIS(Fest).py
'''

import sys
input = sys.stdin.readline

from bisect import bisect_left #내부 함수, 이진탐색의 시간복잡도는 O(logN)이다. bisect_left는 lowerbound

def getDP_LIS(seq):
    A = [-1000000001] #상수는 아니지만 이해를 위해 예시대로 대문자로 간다.

    for x in seq:
        if A[-1]<x: #마지막 숫자 비교
            A.append(x) # 추가
        else:
            A[bisect_left(A,x)]=x #갱신
            
    return A


# 입력
N = int(input()) # 수열 크기
seq = list(map(int,input().split())) #수열

#출력
print(len(getDP_LIS(seq))-1)

'''
범위가 바뀜 = 0을 -1000000001로. 끝
'''