import sys
input = sys.stdin.readline
from collections import deque

def bfs(i):
    q = deque()
    q.append(i)

    visited = [0]*(N+1)
    visited[i] = 1

    cnt = 0
    while q:
        cnt += 1
        cur = q.popleft()
        for next in graphs[cur]:
            if not visited[next]:
                q.append(next)
                visited[next] = 1

    # 크기 비교용 자리기 때문에 제대로 반환할 필요 없다.
    return cnt

# 입력
N, M = map(int, input().split())

graphs = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graphs[b].append(a)

# 출력
max_cnt = 0
answers = list()
for i in range(1, N+1):
    ret = bfs(i)
    if ret > max_cnt:
        answers = [i]
        max_cnt = ret
    elif ret == max_cnt:
        answers.append(i)

answers.sort()
print(*answers)

'''
문제 잘 못 읽었다가 헛고생함
pypy 아니면 시간 초과. 뭘 잘못풀었는듯
'''