'''
대충 위상정렬로 흐름을 읽는 정석적인 문제 같은데...
오랜만인거 같다!
'''
import sys
input = sys.stdin.readline
from collections import defaultdict, deque


# 가수의 수, 보조 PD의 수
N, M = map(int, input().split())
inDegree = [0] * (N+1)
graphs = defaultdict(list)

# 입력 (위상 & 다음)
for _ in range(M):
    singer = list(map(int, input().split()))[1:]
    for i in range(1, len(singer)):
        graphs[singer[i - 1]].append(singer[i])
        inDegree[singer[i]] += 1

# indegree 0들 전부 Queue에 (아무거나 출력하라고 했으니 중간 제어 없음!)
queue = deque()
for i in range(1, N + 1):
    if inDegree[i] == 0:
        queue.append(i)

# 위상 정렬
result = []
while queue:
    node = queue.popleft()
    result.append(node)
    for i in graphs[node]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            queue.append(i)

# 불가능 하면 도중에 막혀서 이 길이가 안나옴
if len(result) == N:
    print(*result)
else:
    print(0)