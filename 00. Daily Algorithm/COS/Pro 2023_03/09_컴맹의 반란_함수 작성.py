'''
BFS 구현
'''
adj = [[] for _ in range(101)]
visited = [0 for _ in range(101)]
answer = 1

def bfs(start):
    global answer
    q = []
    q.append(start)
    visited[start] = 1
    while len(q):
        cur = q[0]
        q.pop(0)
        for next in adj[cur]:
            if visited[next] == 0:
                visited[next] = 1
                answer += 1
                q.append(next)
                
def solution(n, connect):
    for k in connect:
        adj[k[0]].append(k[1])
        adj[k[1]].append(k[0])
    bfs(1)
    return answer
