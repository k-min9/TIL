'''
학생수 900과 보낼 수 62라는 친구 정보 6200
어중간한 숫자에 의미가 있어보이기는 하는데 잘 모르겠다... 흐음
DFS 무지성 전부 돌기
일단 풀어본적 있는 문제
'''
import sys
input = sys.stdin.readline

def dfs(v, arr):
    if len(arr)==K:
        for num in arr:
            print(num)
        exit()

    for i in range(v+1,N+1):
        if not visited[i]:
            for num in arr:
                if num not in graph[i]:
                    break
            else:
                visited[i] = True
                dfs(i, arr+[i])



K, N, F = map(int, input().split())
graph = {i: [] for i in range(1,N+1)}
for _ in range(F):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

for i in range(1, N+1):
    visited = {i: False for i in range(1, N+1)}
    visited[i] = True
    dfs(i, [i])

print(-1)

'''
승주씨 수고하셨어요! 
분리 집합 안될 이유가 있나?
'''
