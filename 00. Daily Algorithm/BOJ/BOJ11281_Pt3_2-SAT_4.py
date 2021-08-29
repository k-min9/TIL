'''
2-SAT : 각 변수 중에 true or false 입력시, 전체(f)가 true가 되는 경우의 수가 있는지 확인 하는 문제
CNF(Conjunctive Normal Form)형태의 식 중 각 절의 최대 변수 수가 2이하이면 2-SAT가 된다.
학습 자료 : https://blog.naver.com/kks227/220803009418
'''
import sys
from collections import deque
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

def my_transform(x):
    if x < 0:
        return -x + N
    else:
        return x

N, M = map(int, input().split())

# 노드 원본과 not 노드
graphs = [[] for _ in range(2*N+1)]
# 각 절 내용 물을 graph에 주입
for _ in range(M):
    a, b = map(int, input().split())
    # graphs[my_transform(-a)].append(my_transform(b))
    # graphs[my_transform(-b)].append(my_transform(a))
    graphs[-a].append(b%(2*N+1))
    graphs[-b].append(a%(2*N+1))

# print(graphs)

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

# print(scc_all)
print(scc_num)


# 2. SAT 풀기
answers = [0]*N
for i in range(1, N+1):
    # 원본과 not이 같은 곳에 소속됨 = 답이 없음
    if scc_num[i] == scc_num[-i]:
        print(0)
        break
    # 그 외에는 무조건 답이 있음. 
    # scc_num이 큼 = DAG상에서 앞에 있음 = not x가 False = x가 True면 무조건 명제 성립
    elif scc_num[i] < scc_num[-i]:
        answers[i-1] = 1
else:
    print(1)
    print(*answers)