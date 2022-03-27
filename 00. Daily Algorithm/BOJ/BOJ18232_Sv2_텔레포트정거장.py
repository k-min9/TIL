'''
S -> E로 이동, 그래프 외에 X+1, X-1 이동이 가능
시간 문제 : BFS가 속이 편함
'''
import sys
input = sys.stdin.readline
from collections import deque


def bfs(start):
    que = deque()
    que.append((start, 0))
    visited = [0] * (N+1)
    while que:
        cur, d = que.popleft()
        if cur == E:
            return d
        if 1 <= cur <= N:
            if not visited[cur]:
                visited[cur] = 1
                que.append((cur+1, d+1))
                que.append((cur-1, d+1))
                for next in graphs[cur]:
                    que.append((next, d+1))

# 입력
N, M = map(int, input().split())
S, E = map(int, input().split())
graphs = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)
print(bfs(S))

'''
이제는 숨쉬듯이 하는 BFS 
+ 못 만나는 경우의 수를 고려하지 않아도 되서 코드가 더 짧아짐.
'''