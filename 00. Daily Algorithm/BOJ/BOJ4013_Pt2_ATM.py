'''
진짜 SCC 단위 위상 정렬
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


# 교차로 수 , 도로 수
N, M = map(int, input().split())
graphs = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    graphs[start].append(end)
moneys = [int(input()) for _ in range(N)]

# 시작 위치, 레스토랑 갯수
start, P = map(int, input().split())
restaurant = list(map(int, input().split()))

# DFS 진행하면서 이곳에 담는다.
stack = []
# visited 없이, SCC에 묶였는지만 확인하여 finished 부여
finished = [0] * (N+1)
# dfsn 또는 id : 스택에 들어간 번호 순서를 의미한다. 간선 순서 파악에 사용
ids = [0] * (N+1)
# 이거 증가시켜가며 노드에게 id를 부여한다.
cnt = 0  
# 총 SCC 숫자와 목록(2차원)과 각각 소속된 번호(index from 0)
scc_cnt = 0
scc_all = list()
scc_num = [0] * (N+1)

# 1. SCC 실행
for i in range(1, N+1):
    if ids[i] == 0:
        tarjan(i)

# print(scc_all)
# print(scc_cnt)
# print(scc_num)

# 2. SCC 합치기

# 레스토랑 배치 여부
restaurant_point = [0] * (N + 1)
for r in restaurant:
    restaurant_point[r] = 1

scc_start = 0
scc_moneys = [0] * scc_cnt
scc_graphs = [[] for _ in range(scc_cnt)]
scc_indegree = [0] * scc_cnt
scc_restaurant = [0] * scc_cnt

# 합치기 작업
for i in range(1, N+1):
    # 소속 번호 확인
    scc_idx = scc_num[i]
    # SCC 내 돈 모으기
    scc_moneys[scc_idx] += moneys[i-1]
    # 거기에 레스토랑 있으면 그 SCC는 레스토랑을 소유한 것
    if restaurant_point[i]:
        scc_restaurant[scc_idx] = 1
    # SCC 번호로 스타트 갱신
    if i == start:
        scc_start = scc_idx
    
    for j in graphs[i]:
        # SCC 밖으로 나가는 degree들 체크
        if scc_idx == scc_num[j]:
            continue
        scc_graphs[scc_idx].append(scc_num[j])
        scc_indegree[scc_num[j]] += 1

# print(scc_start)
# print(scc_moneys)
# print(scc_graphs)
# print(scc_indegree)
# print(scc_restaurant)

# 3. 위상 정렬 시작
scc_dp = scc_moneys[:] # 얕은 복사
scc_visited = [0] * scc_cnt
scc_visited[scc_start] = 1

que = deque()
for i in range(scc_cnt):
    if scc_indegree[i] == 0:
        que.append(i)

# print(scc_dp)
# print(scc_moneys)

while que:
    q = que.popleft()
    for i in scc_graphs[q]:
        if scc_visited[q]:
            scc_dp[i] = max(scc_dp[i], scc_dp[q] + scc_moneys[i])
            scc_visited[i] = 1
        scc_indegree[i] -= 1
        if scc_indegree[i] == 0:
            que.append(i)

# print(scc_dp)
# print(scc_moneys)
# print(scc_visited)

# 결과 = 스타트에서 방문함 + 레스토랑 존재하는 곳 중에 가장 높은 DP값
answer = 0
for i in range(scc_cnt):
    if scc_visited[i] and scc_restaurant[i]:
        answer = max(answer, scc_dp[i])

print(answer)
