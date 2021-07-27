'''
일단 전제는 다익스트라고
힘으로 해결되나 부터 확인하는건 어떰?
노드를 하나씩 뽑아보는거지
'''
'''
다익스트라 복습
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
5. 3, 4 반복
'''

# 전처리
import sys
input = sys.stdin.readline
from heapq import heappop, heappush

# 자료 구조 버전
def dijkstra(nodeStart, block1 = 0, block2 = 0):

    INF = 1e9 #무한을 대체할 값
    distance = [INF] * (N + 1) #start 노드로부터 최단거리테이블 초기화
    q = []
    heappush(q, [0, nodeStart]) # distance, idx
    distance[nodeStart] = 0 #출발이니 0
    while q: #큐가 비어있지 않다면
        #가장 가까운 최단거리 노드 정보 pop
        dist, nodeClose = heappop(q)
        #이미 처리 되었을 경우 다음 루프
        if distance[nodeClose] < dist:
            continue
        #현재 노드와 연결된 다른 노드 확인
        for i in graph[nodeClose]:
            # 이 문제의 도로검문 파트
            if block1 == nodeClose and block2 == i[0] or block2 == nodeClose and block1 == i[0]:
                continue
            cost = dist+ i[1] # 현 시점에서 dist = distance[nodeClose]
            # if block1 == 0: #간선 기록 모드(2307)
            #     print('routeA', i[0], nodeClose)
            #     rm[i[0]] = nodeClose
            #현재 노드를 거치는게 더 짧을 경우 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, [cost, i[0]])
                if block1 == 0: #간선 기록 모드(2307)
                    #print('routeB', i[0], nodeClose)
                    rm[i[0]] = nodeClose
    return distance[-1] #최단 거리 테이블의 마지막 정보만 반환


#노드의 개수, 간선의 개수
N, M = map(int, input().split())

#트리(그래프) 정보 입력용 리스트
graph = [[] for _ in range(N + 1)]

#통제 정보
#rm = []
rm = [0] * (N+1) # 어디서 왔는지 기록

#간선의 개수(M) 만큼 정보 입력
for _ in range(M):
    nodeA, nodeB, dist = map(int,input().split())
    graph[nodeA].append((nodeB,dist)) # treeA에서 treeB까지의 거리 dist (미방향 노드)
    graph[nodeB].append((nodeA,dist)) # treeB에서 treeA까지의 거리 dist (미방향 노드)
    #rm.append([nodeA, nodeB]) # 검문 통제 정보

#통제 없을때 시간
answer1 = dijkstra(1)
# print(answer1)
#print('rm', rm)

#통제 있을때 시간
answer2= 0

'''
from copy import deepcopy
deepcopy 처음 써봄 <<< 시간 초과
#통제의 시간이다!
for r in rm:
    graph2 = deepcopy(graph)
    graph2[r[0]].remove((r[1], r[2]))
    graph2[r[1]].remove((r[0], r[2]))
    answer2 = max(answer2, dijkstra(1, graph2))

# print(answer2)
'''
'''
2차 시도 <<< 시간 초과. 아니 꽤 깔끔하다고 보는데;;
#통제의 시간이다! ver2
for r in rm:
    answer2 = max(answer2, dijkstra(1, r[0], r[1]))
'''

next = N
while(next!=1):
    answer2 = max(answer2, dijkstra(1, rm[next], next))
    next = rm[next]

if answer2 != 1e9:
    print(answer2 - answer1)
else:
    print(-1)

'''
3차 시도 : 결국 인터넷 뒤져서 나온 최고 효율이 나온 간선 부분만을 체크하는 방식, 
그렇게 큰 시간차이 안 날 줄 알았는데 엄청 났다. 이래서 푼 문제도 꼭 다시 찾아봐야 한다.
대충 1차 ~ 3차까지 M*M -> rm -> M 수준으로 절약.
근데 몇번이나 고쳤더니 완전 코드가 누더기가 됨 ㅋㅋㅋㅋ
*p.s. python이 pypy보다 빨랐음. 이거 차이 발생 요인 같은거 대략적인거 조금 알아두면 아슬아슬한거 풀 때 편할 것 같다.
'''