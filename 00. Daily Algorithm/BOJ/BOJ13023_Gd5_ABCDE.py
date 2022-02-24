'''
ABCDE가 정해진게 아니라 그냥 깊이 4 이상인 친구 관계가 있는 문제였다. 하...
'''
import sys
input = sys.stdin.readline


def dfs(v, depth):
    global answer
    visited[v] = 1

    if depth >= 4:
        answer = 1
        return
    if answer:
        return

    for node in graph[v]:
        if not visited[node]:
            dfs(node, depth + 1)
            visited[node] = 0



n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * n
answer = 0
for i in range(n):
    dfs(i, 0)
    visited[i] = 0
    if answer:
        break

print(answer)
