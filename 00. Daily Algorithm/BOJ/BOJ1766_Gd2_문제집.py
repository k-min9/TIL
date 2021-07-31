'''
오름차순 위상정렬 >>> 최소 heap
'''

import sys
input = sys.stdin.readline

from heapq import heappop, heappush

# anw 비교 횟수(간선 수)
N, M = map(int, input().split())

# 정보 정리
inDeg = [0] * (N+1)  # 진입차수
graph = [[] for _ in range(N+1)]

# 그래프 그리기
for _ in range(M):
    a, b = map(int, input().split())  # a에서 b로 정렬
    inDeg[b] = inDeg[b] + 1
    graph[a].append(b)

# 큐 세팅
que = []
for i in range(1,N+1):
    if inDeg[i] == 0:
        heappush(que, i)


# 위상 정렬
answer = []
while que:
    q = heappop(que)
    answer.append(q)  # 솔직히 여기서 print(q, end='')쓰면 answer 필요 없어질 듯
    for i in graph[q]:  # 그래프 돌면서 화살표 해제
        inDeg[i] = inDeg[i] - 1
        if inDeg[i] == 0:
            heappush(que, i)

print(*answer)

'''
나 이거랑 똑같은 문제 어디서 푼거 같은데;;
'''