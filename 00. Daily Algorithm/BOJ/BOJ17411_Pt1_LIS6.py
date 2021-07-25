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
'''
07.25. 다음날 돌아왔다. 형님도 데려왔다.
https://stackoverflow.com/questions/22923646/number-of-all-longest-increasing-subsequences
'''
'''
60%의 벽을 못넘고 메모리 초과 후퇴!
'''

import sys
input = sys.stdin.readline

from bisect import bisect_left#내부 함수, 이진탐색의 시간복잡도는 O(logN)이다. bisect_left는 lowerbound
from collections import deque

# 함수 개조(Desc 개조)
def my_bisect_right(a, x, lo=0, hi=None):
    hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x >= a[mid]: hi = mid
        else: lo = mid+1
    return len(a) - lo


#입력
N = int(input()) # 수열 크기
seq = list(map(int,sys.stdin.readline().split())) #수열

A = [-1000000001] #상수는 아니지만 이해를 위해 예시대로 대문자로 간다.
dp1 = deque() #i까지 LIS길이

for x in seq:
    if A[-1]<x: #마지막 숫자 비교
        dp1.append([x, len(A)])
        A.append(x) # 추가            
    else:
        idx = bisect_left(A,x)
        dp1.append([x, idx])
        A[idx]=x #갱신

routedIdx = len(A)-1
#del(A)

#루트 sum 기록 dp
dp2 = [[0] for _ in range(routedIdx + 1)] #count=>sum

#이진 탐색용 기록 dp
dp3 = [[] for _ in range(routedIdx + 1)]

while dp1:

    x = dp1.popleft()
    dp3[x[1]].append(x[0])

    if x[1] != 1:
        count1 = dp2[x[1]-1][-1] #전 행의 마지막 sum
        # print('dpp', dp3[x[1]-1],x[0])
        #dp3[x[1]-1].sort() # 쓸모없는 연산, 이거 싫으면 내림차순용 bisect 만드셈.
        bisectNum = my_bisect_right(dp3[x[1]-1],x[0]) + 1
        #print('bisect', x[0],bisectNum, dp3[x[1]-1])
        count2 = dp2[x[1]-1][-bisectNum] #전 행의 그 전 sum
        count3 = dp2[x[1]][-1] # 같은 행의 마지막 sum
        sum = count1 - count2 + count3
    else:
        #print('dp2', dp2)
        count3 = dp2[x[1]][-1] # 같은 행의 마지막 sum
        sum = 1 + count3
    dp2[x[1]].append(sum)

print(routedIdx, dp2[-1][-1] % 1000000007)


'''
N-1차 도전 : 변경 안될 정보인 dp1 내용물 덱으로 변경. del(A)추가
N-2차 도전 : 잘 가다가 메모리 초과. 거의 다 왔다. 아마 마지막 단계. dp2 정보를 반을 줄인다.
import sys
input = sys.stdin.readline

from bisect import bisect_left#내부 함수, 이진탐색의 시간복잡도는 O(logN)이다. bisect_left는 lowerbound

# 함수 개조(Desc 개조)
def my_bisect_right(a, x, lo=0, hi=None):
    hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x >= a[mid]: hi = mid
        else: lo = mid+1
    return len(a) - lo


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

routedIdx = len(A)-1

#루트 sum 기록 dp
dp2 = [[[0,0]] for _ in range(routedIdx + 1)] #count=>sum

#이진 탐색용 기록 dp
dp3 = [[] for _ in range(routedIdx + 1)]

for x in dp1:

    dp3[x[1]].append(x[0])

    if x[1] != 1:
        count1 = dp2[x[1]-1][-1][1] #전 행의 마지막 sum
        # print('dpp', dp3[x[1]-1],x[0])
        #dp3[x[1]-1].sort() # 쓸모없는 연산, 이거 싫으면 내림차순용 bisect 만드셈.
        bisectNum = my_bisect_right(dp3[x[1]-1],x[0]) + 1
        #print('bisect', x[0],bisectNum, dp3[x[1]-1])
        count2 = dp2[x[1]-1][-bisectNum][1] #전 행의 그 전 sum
        count3 = dp2[x[1]][-1][1] # 같은 행의 마지막 sum
        sum = count1 - count2 + count3
    else:
        count3 = dp2[x[1]][-1][1] # 같은 행의 마지막 sum
        sum = 1 + count3
    new = [x[0]] + [sum]
    #print('new', new)
    dp2[x[1]].append(new)
#print(dp2)

print(routedIdx, dp2[-1][-1][1] % 1000000007)
'''

'''
X차 도전 : 내림차순에서는 bisect 안먹힌다는걸 배웠다. 진짜 비싼 교훈.
'''






'''
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

'''







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