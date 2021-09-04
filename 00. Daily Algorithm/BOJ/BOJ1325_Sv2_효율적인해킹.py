import sys
input = sys.stdin.readline
from collections import deque

def bfs(i):
    q = deque()
    q.append(i)

    visited = [0]*(N+1)
    visited[i] = 1

    while q:
        cur = q.popleft()
        for next in graphs[cur]:
            if not visited[next]:
                q.append(next)
                visited[next] = visited[cur] + 1

    # 크기 비교용 자리기 때문에 제대로 반환할 필요 없다.
    return max(visited) + 1

# 입력
N, M = map(int, input().split())

# indegree 0 모음
graphs = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graphs[b].append(a)

max_cnt = 0
answers = list()
for i in range(1, N+1):
    ret = bfs(i)
    if ret > max_cnt:
        answers = list()
        max_cnt = ret
        answers.append(i)
    elif ret == max_cnt:
        answers.append(i)

answers.sort()
print(*answers)

'''
문제 잘 못 읽었다가 헛고생함
'''