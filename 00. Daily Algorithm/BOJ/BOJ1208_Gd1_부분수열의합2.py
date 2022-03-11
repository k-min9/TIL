'''
밋 인 더 미들의 대표 문제로 소개 받음!
1. 주어진 수열을 반으로 나누고
2. 나눠진 수열의 부분 수열을 구하고
3. A의 부분 수열 중 하나를 선택하고, B의 부분 수열 중 하나를 선택하면 모든 부분 수열을 구할 수 있음
4. 그 합을 배열에 저장
'''
import sys
from itertools import combinations
from collections import defaultdict

n,s=map(int,sys.stdin.readline().split())
m=list(map(int, sys.stdin.readline().split()))


l=m[:n//2]
r=m[n//2:]

lsum=defaultdict(int)
rsum=defaultdict(int)
lsum[0]=1
rsum[0]=1
for i in range(1,len(l)+1):
    for com in combinations(l,i):
        lsum[sum(com)]+=1

for i in range(1,len(r)+1):
    for com in combinations(r,i):
        rsum[sum(com)]+=1

lkey=sorted(lsum.keys())
rkey=sorted(rsum.keys())

res=0
l=0
r=len(rkey)-1
while l<len(lkey) and r>=0:
    if lkey[l]+rkey[r]==s:
        res+=(lsum[lkey[l]]*rsum[rkey[r]])
        l+=1
        r-=1
    elif lkey[l]+rkey[r]>s:
        r-=1
    else:
        l+=1

if s==0:
    res-=1
print(res)

'''
학습 완료!!!
'''