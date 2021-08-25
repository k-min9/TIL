'''
강한 연결 요소 (Strongly Connected Component)
어떤 두 정점을 골라도 가는 경로가 존재하는 그래프 분리 방식
그렇게 그래프를 SCC 단위로 압축하여 하나의 정점으로 취급하면,
그 그래프는 반드시 DAG이다. 즉 위상정렬을 사용할 수 있게 된다.
(DAG : 비순환(사이클 없는) 일방향 그래프)
알고리즘은 Tarjan 알고리즘이 제네릭하고 Kosaraju보다 빠르다. O(V+E)
https://ca.ramel.be/166
https://blog.naver.com/kks227/220802519976
'''

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
        answers.append(sorted(SCC))

V, E = map(int, input().split())
graphs = [[] for _ in range(V+1)]
for _ in range(E):
    start, end = map(int, input().split())
    graphs[start].append(end)

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
print(len(answers))
for i in sorted(answers):
    print(*i, -1)

'''
4196 도미노에서 실제 위상정렬 적용 해봄
'''

'''
0. low 배열을 쓰지 않고 리턴으로 받는 방법 
메모리 사용량은 거의 비슷하지만 약간 더 빠르다.
answers에 0이 담기고 초기값을 더 주의해야 되는건
visited를 직접 미로 풀이에 이용하는 DFS가 생각나는데 딱 그런 느낌이 맞는것 같다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def tarjan(x):
    # 노드에 low와 id 부여
    global cnt
    cnt += 1
    ids[x] = cnt

    # DFS 방문 순서대로 stack에 담는다.
    stack.append(x)

    # 역간선 및 finished 체크. 같은 값을 가진 노드끼리 SCC로 묶인다.
    low = cnt

    for next in graphs[x]:
        # 아이디 미부여 = 방문 안 함 = 계속 DFS 전진, 이거 그냥 visited 쓰지??
        if ids[next] == 0:
            # DFS 끝나고 간선 복귀 시(역간선) 갱신됨
            low = min(low, tarjan(next))
        # 다음 갈 곳을 방문함 = DFS 재귀 종료 시점
        elif not finished[next]:
            low = min(low, ids[next])
    
    # DFS 재귀가 종료 -> low가 같은데로 묶는다.
    if low == ids[x]:
        cur_scc = list()
        while True:
            w = stack.pop()
            cur_scc.append(w)
            # w는 SCC로 묶임을 표기
            finished[w] = 1
            if w == x:
                break
        answers.append(sorted(cur_scc))

    # 여기서 리턴하니까 low 배열을 안 쓰는 것
    return low

V, E = map(int, input().split())
graphs = [[] for _ in range(V+1)]
for _ in range(E):
    start, end = map(int, input().split())
    graphs[start].append(end)

# DFS 진행하면서 이곳에 담는다.
stack = []
# visited 없이, SCC에 묶였는지만 확인하여 finished 부여
finished = [0] * (V+1)
# dfsn 또는 id : 스택에 들어간 번호 순서를 의미한다. 간선 순서 파악에 사용
ids = [0] * (V+1)
# 이거 증가시켜가며 노드에게 id를 부여한다.
cnt = 0  

# 시작
answers = list()

for i in range(V):
    if ids[i] == 0:
        tarjan(i)
print(len(answers) - 1)
for i in sorted(answers[1:]):
    print(*i, -1)


'''