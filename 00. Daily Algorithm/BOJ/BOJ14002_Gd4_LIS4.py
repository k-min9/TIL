'''
<가장 긴 증가하는 부분 수열(Longest Increasing Subsequence aka.LIS) 축제>
~ on 2021.07.24 from BOJ11053_Sv2_LIS(Fest).py
'''

import sys
input = sys.stdin.readline

from bisect import bisect_left #내부 함수, 이진탐색의 시간복잡도는 O(logN)이다. bisect_left는 lowerbound

def getDP_LIS(seq):
    A = [0] #상수는 아니지만 이해를 위해 예시대로 대문자로 간다.
    dp = []

    for x in seq:
        if A[-1]<x: #마지막 숫자 비교
            dp.append([x, len(A)])
            A.append(x) # 추가            
        else:
            idx = bisect_left(A,x)
            dp.append([x, idx])
            A[idx]=x #갱신

    return A, dp


#입력
N = int(input()) # 수열 크기
seq = list(map(int,input().split())) #수열

#LIS
answer, dp = getDP_LIS(seq)

#경로 입력
routeIdx = len(answer) - 1
route = []
for i in range(N-1,-1,-1):#뒤에서부터 줍기
    if dp[i][1] == routeIdx:
        route.append(dp[i][0])
        routeIdx = routeIdx - 1    

#출력
print(len(answer)-1)
route.reverse()
print(*route)



'''
표를 재현하고, 뒤에서부터 줏어오면 된다.
'''