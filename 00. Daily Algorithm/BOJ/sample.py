import sys
from bisect import bisect_left
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

q=[arr[0]]
t=[] # (들어갈 위치, 값)의 쌍을 넣는 배열
# 여기는 이전 문제들과 비슷하다.
#  다만 t라는 새로운 배열에 갱신되는 배열 요소의 위치, 요소 값에 대한 정보도 추가하는게 다르다
for x in arr:
    
    if q[-1]<x:
        q.append(x)
        t.append((len(q)-1,x))
    else:
        idx=bisect_left(q,x)
        q[idx]=x
        t.append((idx,x))
        print(idx)
print(t)        
# 최종 배열의 길이를 구했으면 마지막 위치부터 가장 큰 요소를 넣는다 (실제 요소)       
last_idx=len(q)-1

# 덮어씌워진 요소가 아니라 기존 요소를 넣어준다 
ans=[]
for i in range(n-1,-1,-1):
    if t[i][0]==last_idx:
        ans.append(t[i][1])
        last_idx-=1

# print(q)
# print(t)
print(len(q))
# *을 붙이면 자동으로 리스트 요소를 공백으로 구분해 반환해준다
print(*reversed(ans))