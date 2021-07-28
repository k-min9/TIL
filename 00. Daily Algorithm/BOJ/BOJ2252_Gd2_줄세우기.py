'''
위ㅡ상ㅡ정ㅡ렬ㅡ 
준비물 : 큐
'''

import sys
input = sys.stdin.readline

from collections import deque

# 학생 수, 비교 횟수(간선 수)
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
que = deque()
for i in range(1,N+1):
    if inDeg[i] == 0:
        que.append(i)

# 위상 정렬
answer = []
while que:
    q = que.popleft()
    answer.append(q)  # 솔직히 여기서 print(q, end='')쓰면 answer 필요 없어질 듯
    for i in graph[q]:  # 그래프 돌면서 화살표 해제
        inDeg[i] = inDeg[i] - 1
        if inDeg[i] == 0:
            que.append(i)

print(*answer)