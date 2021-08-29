'''
여기까지 길었음. 이거 하나 풀려고
SCC랑 2-SAT 학습하고 왔습니다. 간다!
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def tarjan(x):
    # 노드에 low와 id 부여
    global cnt, scc_cnt
    cnt += 1
    ids[x] = cnt

    # DFS 방문 순서대로 stack에 담는다.
    stack.append(x)

    # 역간선 및 finished 체크. 같은 값을 가진 노드끼리 SCC로 묶인다.
    low = cnt

    for next in graphs[x]:
        # 아이디 미부여 = 방문 안 함 = 계속 DFS 전진, DFS 끝나고 간선 복귀 시(역간선) 갱신됨
        if ids[next] == 0:
            low = min(low, tarjan(next))
        # 다음 갈 곳을 방문함 = DFS 재귀 종료 시점
        elif not finished[next]:
            low = min(low, ids[next])
    
    # DFS 재귀가 종료 -> low가 같은데로 묶는다.
    if low == ids[x]:
        scc_cur = list()
        while True:
            w = stack.pop()
            scc_cur.append(w)
            finished[w] = 1 # w는 SCC로 묶임을 표기
            scc_num[w] = scc_cnt # 소속된 SCC 번호
            if w == x:
                break
        scc_all.append(scc_cur)
        scc_cnt += 1

    # 여기서 리턴하고 low 배열을 안 씀
    return low

# 개구리 수, 통나무 수
N, M = map(int, input().split())
# 주제별 흥미도
status = [0] + [list(map(int, input().split())) for _ in range(N)]
# 연꽃의 수요
demands = [[] for _ in range(N+1)]
positions = []
for i in range(N):
    a, b = map(int, input().split())
    #첫번째 연꽃이 True 두번째 연꽃이 False
    demands[a].append(i+1)
    demands[b].append(-(i+1))
    # 나중에 2SAT 결과 True면 b, False면 a 가 선택이 된다.
    positions.append((a, b))

# print(demands)

cnf = []
for demand in demands:
    n = len(demand)
    for i in range(n):
        for j in range(i+1, n):
            cnf.append((demand[i], demand[j]))

for i in range(M):
    # 연꽃 1, 2, 대화주제
    a, b, t = map(int, input().split())
    for x in demands[a]:
        for y in demands[b]:
            # 취미값이 다를 경우, x가 올라가는 경우, y는 올라가지 못함.
            if status[abs(x)][t-1] != status[abs(y)][t-1]:
                cnf.append((x, y))


graphs = [[] for _ in range(2*N+1)]
# 각 절 내용 물을 graph에 주입
for a, b in cnf:
    graphs[-a].append(b%(2*N+1))
    graphs[-b].append(a%(2*N+1))


# 타잔 준비물 시작=====================
# DFS 진행하면서 이곳에 담는다.
stack = []
# visited 없이, SCC에 묶였는지만 확인하여 finished 부여
finished = [0] * (2*N+1)
# dfsn 또는 id : 스택에 들어간 번호 순서를 의미한다. 간선 순서 파악에 사용
ids = [0] * (2*N+1)
# 이거 증가시켜가며 노드에게 id를 부여한다.
cnt = 0  
# 총 SCC 숫자와 목록(2차원)과 각각 소속된 번호(index from 0)
scc_cnt = 0
scc_all = list()
scc_num = [0] * (2*N+1)
# 타잔 준비물 종료=======================

# 1. SCC 실행
for i in range(1, 2*N+1):
    if ids[i] == 0:
        tarjan(i)

#print(scc_all)
#print(scc_num)

# 2. SAT 풀기
answers = [0]*N
for i in range(1, N+1):
    # 원본과 not이 같은 곳에 소속됨 = 답이 없음
    if scc_num[i] == scc_num[-i]:
        print("NO")
        break
    # 그 외에는 무조건 답이 있음. 
    # scc_num이 큼 = DAG상에서 앞에 있음 = not x가 False = x가 True면 무조건 명제 성립
    elif scc_num[i] < scc_num[-i]:
        answers[i-1] = 1
else:
    print("YES")
    # print(*answers)
    answers2 = [0]*N
    for i in range(N):
        answers2[positions[i][answers[i]] - 1] = i + 1
    print(*answers2)

'''
네 이거 딱 잡고 플레찍었습니다.
'''