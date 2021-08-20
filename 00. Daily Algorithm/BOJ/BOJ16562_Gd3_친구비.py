'''
그룹핑을 해서 min을 하라는건데... union-find?
아니, 이건 무지성 코딩이다
>> 다시는 그러지 마세요.
>> 내.
'''

import sys
input = sys.stdin.readline
from heapq import heappush

# 서로소 집합 자료구조 (합치기 찾기 자료구조)

# 지원함수 1 : 유니온 - 합치기
def union(a, b):
    a = find(a)
    b = find(b)

    # 갱신 내지 재정의
    if b < a:
        parent[a] = b
    else:
        parent[b] = a

# 지원함수 2 : find - 루트 노드를 찾을때까지 재귀적으로 반환
def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

# 정점 수, 간선 수, 보유 돈
N, M, k = map(int, input().split())
costs = [0] + list(map(int, input().split()))
# 서로소 집합 자료구조용 입력 정보
parent = list(range(N+1))

# 간선 정보 정리
for _ in range(M):
    a, b= map(int, input().split())
    union(a,b)

groups = [[] for _ in range(N+1)]
# 친구별로 부모 체크하면서 최소 heap으로 자동 정리
for i in range(1, N+1):
    heappush(groups[find(i)], costs[i])

ans = 0
for group in groups:
    if group:
        ans += group[0]

if ans <= k:
    print(ans)
else:
    print("Oh no")




'''
>> 1차 시도 : set을 이용한 그루핑 >> 역시 union find 맞잖아!!!

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
costs = [0] + list(map(int, input().split()))

groups = []
cnt = 0

for _ in range(M):
    a, b = map(int, input().split())
    flag = -1
    flag2 = -1
    tmp = list()
    for i in range(cnt):
        if a in groups[i]:
            if flag == -1:
                groups[i].add(b)
                flag = i
            else:
                flag2 = i
                break
        elif b in groups[i]:
            if flag == -1:
                groups[i].add(b)
                flag = i
            else:
                flag2 = i
                break

    if flag == -1:
        cnt = cnt + 1
        groups.append({a, b})
    elif flag2 != -1:
        groups.append(groups[flag]|groups[flag2])
        del groups[max(flag, flag2)]
        del groups[min(flag, flag2)]
        cnt = cnt - 1

print(groups)

ans = 0
for group in groups:
    cost_min = 10000
    for g in group:
        cost_min = min(costs[g], cost_min)
    ans = ans + cost_min
if K >= ans:
    print(ans)
else:
    print("Oh no")
'''