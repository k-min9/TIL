'''
itertools 안쓴 풀이를 원하겠지만 HAHAHA... 피곤해
'''
# 15654
# import sys
# from itertools import permutations
# input = sys.stdin.readline
# N, M = map(int, input().split())
# nums = list(map(int,input().split()))
# for i in permutations(sorted(nums), M): 
#     print(*i)

# 15650
import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(range(1,N+1))
for i in combinations(nums, M): 
    print(*i)


# 15650 안 쓴 풀이
N, M = map(int, input().split())

visited=[0]*N
s=[]

def dfs(a):
    if a == M:
        print(*s)
        return

    for i in range(0, N):
        if a!= 0 and i+1 < s[-1]:
            continue

        if visited[i]:
            continue

        visited[i]=1
        s.append(i+1)

        dfs(a+1)
        s.pop()
        visited[i]=False

# a: 들어간 횟수 = 탐색(조합) 횟수
dfs(0)
