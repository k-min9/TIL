'''
<가장 긴 증가하는 부분 수열(Longest Increasing Subsequence aka.LIS) 축제>
~ on 2021.07.24 from BOJ11053_Sv2_LIS(Fest).py
'''
'''
접근 : 예시로부터 생각해서
입력 : 10 20 30 10 20 30 > 출력 : 3 4
10 20 30 10 20 30
1 1 '1' 0 0 '0'
1 1 '0' 0 0 '1'
1 0 '0' 0 1 '1'
0 0 '0' 1 1 '1'
''한 숫자의 합이 4라는 것을 알 수있다.
즉 DP값이 가장 높은 곳을 마지막으로 하는 것으로 역산해서 전부 더하면 된다.
이 DP값을 count하는 DP를 만들자
'''
'''
언젠간 돌아올 것이야/////
'''


import sys
input = sys.stdin.readline

from bisect import bisect_left, bisect_right #내부 함수, 이진탐색의 시간복잡도는 O(logN)이다. bisect_left는 lowerbound

#입력
N = int(input()) # 수열 크기
seq = list(map(int,input().split())) #수열

A = [-1000000001] #상수는 아니지만 이해를 위해 예시대로 대문자로 간다.
dp1 = [] #i까지 LIS길이

for x in seq:
    if A[-1]<x: #마지막 숫자 비교
        dp1.append([x, len(A)])

        A.append(x) # 추가            
    else:
        idx = bisect_left(A,x)
        dp1.append([x, idx])
        A[idx]=x #갱신

print(dp1)

routeIdx = len(A)-1
num = [[] for _ in range(routeIdx + 1)]
sum = [[0] for _ in range(routeIdx + 1)]

for i in range(N-1,-1,-1):
    j = 1
    length = dp1[i][1]
    if length < routeIdx:
        idx = bisect_right(num[length],dp1[i][0])
        print('idx', idx)
        j = sum[length + 1][-1] - sum[length + 1][idx]
        print('a', sum[length + 1][-1])
        print('j', j)
    num[length].append(dp1[i][0])
    sum[length].append(j)
print(num)
print(sum)




#dp2 = [0] #i까지 그 길이인 LIS 개수






'''
1차시도 <<< 시간 초과. 그야 O(N^2)으로 회귀해버렸으니
def getDP_LIS(seq):
    A = [-1000000001] #상수는 아니지만 이해를 위해 예시대로 대문자로 간다.
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
routeIdx = len(answer) - 1
routeNum = 0
# count : 이 값을 마지막으로 하는 LIS 개수를 DP
count = [0]*N # 초기값, 자기자신
count[0] = 1
for i in range(1,N):
    for j in range(i):
        n = -1000000001
        if dp[j][0]<dp[i][0]:
            n = max(n, dp[j][1])
    for j in range(i):
        if dp[j][1] == n:
            count[i] = count[i] + count[j]
    count[i] = max(count[i],1)
print(dp)
print(count)

for i in range(N):
    if dp[i][1] == routeIdx:
        routeNum = routeNum + count[i]


#출력
print(routeIdx, routeNum%(1000000007))
'''