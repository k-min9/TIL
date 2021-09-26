'''
위상정렬
'''
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
indegree = [0]*(N+1)
times = [0]*(N+1)
graphs = [[] for _ in range(N+1)]
q = deque()

answers = [0]*(N+1)
for i in range(1, N+1):
    infos = list(map(int, input().split()))
    times[i] = infos[0]
    for info in infos[1:-1]:
        indegree[i] += 1
        graphs[info].append(i)
    if indegree[i] == 0:
        q.append(i)
        answers[i] = times[i]

#print(graphs)

while q:
    cur = q.popleft()
    for i in graphs[cur]:
        indegree[i] -= 1
        # 시간 10과 4 + 2가 선행되야하면 여태 누적된 값이 큰 값 + 코스트의 dp
        answers[i] = max(answers[i], times[i] + answers[cur])

        if indegree[i] == 0:
            q.append(i)

for answer in answers[1:]:
    print(answer)
