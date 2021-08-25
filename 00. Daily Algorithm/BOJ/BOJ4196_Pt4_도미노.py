'''
~ from 2150 SCC
SCC를 실제로 활용하여 위상정렬에 사용해 보자.
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def tarjan(x):
    # 노드에 low와 id 부여
    global cnt
    ids[x] = cnt
    low[x] = cnt
    cnt += 1

    # DFS 방문 순서대로, 스택에 담고 visited 표시
    visited[x] = 1
    stack.append(x)

    for next in graphs[x]:
        # 아이디 미부여 = 방문 안 함 = 계속 DFS 전진, 이거 그냥 visited 쓰지??
        if ids[next] == -1:
            tarjan(next)
            # DFS 끝나고 간선 복귀 시 갱신됨
            low[x] = min(low[x], low[next])
        # 다음 갈 곳을 방문함 = DFS 재귀 종료 시점
        elif visited[next] == 1:
            low[x] = min(low[x], low[next])
    
    # 모든 DFS 재귀가 종료 -> low가 같은데로 묶으면 끝
    SCC = list()
    # 각 SCC의 시작 지점
    w = -1
    if low[x] == ids[x]:
        while w != x:
            w = stack.pop()
            SCC.append(w)
            visited[w] = -1  # 이거 안하면 다음 DFS때 visited[next] == 1에서 low가 전염됨
        answers.append(SCC)

# 테스트 케이스 수
T = int(input())
for _ in range(T):
    # 도미노 수, 도미노 관계 수
    V, E = map(int, input().split())
    graphs = [[] for _ in range(V+1)]
    indegree = [0] * (V + 1)
    for _ in range(E):
        start, end = map(int, input().split())
        graphs[start].append(end)
        indegree[end] += 1

    # DFS 진행하면서 이곳에 담는다.
    stack = []
    visited = [0] * (V+1)
    # 역간선 및 finished 체크 같은 값을 가진 노드끼리 SCC로 묶인다.
    low = [-1] * (V+1)
    # dfsn 또는 id : 스택에 들어간 번호 순서를 의미한다. 간선 순서 파악에 사용
    ids = [-1] * (V+1)
    cnt = 0  # 이거 증가시켜가며 노드에게 id를 부여한다.

    # 시작
    answers = list()

    for i in range(1, V+1):
        if ids[i] == -1:
            tarjan(i)

    # 이제 answers는 SCC대로 묶였다.
    answer = 0
    for scc in answers:
        if len(scc) == 1:
            if indegree[scc[0]] == 0:
                answer = answer + 1
        else:
            flag = True
            for s in scc:
                # 외부 SCC로부터의 진입이 있음
                if indegree[s] > 1:
                    flag = False
            if flag:
                answer = answer + 1
    print(max(answer, 1))