'''
이 작업을 끝내기 위해 먼저해야하는 작업 수
> 뒤집어서 제출하면 끝...
'''
import sys
input = sys.stdin.readline

# 작업 갯수와 작업 정보수
N, M = map(int, input().split())
graphs = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graphs[y].append(x)
todo = int(input())

todos = [todo]
done = set()

answer = 0
while todos:
    now = todos.pop()
    for next in graphs[now]:
        if next not in done:
            done.add(next)
            answer += 1
            todos.append(next)

print(answer)
