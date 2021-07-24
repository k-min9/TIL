'''
<가장 긴 증가하는 부분 수열(Longest Increasing Subsequence aka.LIS) 축제>
~ on 2021.07.24 from BOJ11053_Sv2_LIS(Fest).py
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
seq = list(map(int,input().split())) #수열

#출력
print(len(getDP_LIS(seq))-1)

'''
N이 1000에서 1000000으로 늘었다.
LIS 1때와 같은 알고리즘으로 풀면 시간초과 된다.
bisect를 이용한 정렬로 복잡도 문제를 해결할 수 있다.
이렇게 바꿀 경우, 시간 복잡도 O(n^2)에서 O(nlogn)까지 낮출 수 있다.

위키를 참조하는건 조금 걸리는데 
그래도 : https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4
'''