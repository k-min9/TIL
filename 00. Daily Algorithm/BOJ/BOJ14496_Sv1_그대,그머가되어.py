'''
최소거리 뽑는거면 다익스트라 내지 BFS 추천인데
'''
import sys
from heapq import heappush, heappop
input = sys.stdin.readline


# 상수
MAX = 987654321

# 입력
a, b = map(int, input().split())
N, M = map(int, input().split())  # 전체 문자 수, 치환 가능한 문자쌍 수
graphs = [[] for _ in range(N+1)]
# print(graphs)
for _ in range(M):
    x, y= map(int, input().split())
    graphs[x].append(y)
    graphs[y].append(x)

dists = [MAX] * (N+1)
dists[a] = 0
que = list()
heappush(que, (0, a))
while que:
    dist, cur_node = heappop(que)
    if dists[cur_node] < dist:
        continue

    for next_node in graphs[cur_node]:
        if dists[next_node] > dist + 1:
            dists[next_node] = dist + 1
            heappush(que, (dist+1, next_node))

if dists[b] == MAX:
    dists[b] = -1
print(dists[b])

'''
네 다익스트라
'''