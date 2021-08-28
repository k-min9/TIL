'''
최대 힙 쓰면 되는거 아님???
'''

# from heapq import heappush, heappop

# N, M = map(int, input().split())
# s, e = map(int, input().split())

# graphs = [[] for _ in range(N+1)]
# for _ in range(M):
#     a, b, x = map(int, input().split())
#     graphs[a].append((-x, b))
#     graphs[b].append((-x, a))

# # 최대 힙으로 최대한 챙기며 이동
# que = [(-1000000, s)]
# visited = [0]*(N+1)
# while True:
#     x, a = heappop(que)
#     visited[a] = -x
#     if a == e:
#         break
#     else:
#         for nx, na in graphs[a]:
#             if not visited[na]:
#                 heappush(que, (nx, na))

# print(visited[e])

'''
오늘 영 아니네... 스터디 동료 풀이 리팩토링
이진법 + 최대 리미트를 비교한다는 부분 은 결정 문제 풀이지만
최대 힙으로 접근 했던 방식과 매우 풀이가 유사해서 바로 이해했다.
'''
import sys
input = sys.stdin.readline
from collections import deque

def is_possible(limit):
    queue = deque()
    queue.append(s)

    visited = [0]*(N+1)
    visited[s] = True

    while queue:
        cur_node = queue.popleft()
        if cur_node == e:
            return True
        for next_node, next_limit in graph[cur_node]:
            if not visited[next_node] and limit <= next_limit:
                visited[next_node] = True
                queue.append(next_node)
    return False

N, M = map(int, input().split())
s, e = map(int, input().split())
graph = {i: [] for i in range(1,N+1)}
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

left = 1
right = 1000000
answer = 0
while left <= right:
    mid = (left + right)//2
    if is_possible(mid):
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(answer)