'''
감상 : 루트 적으면 메모리 부족하다 엔딩일거 같고...
일단 트라이 
1. route = [[] for _ in range(MAX+1)] 2차원 리스트 참패
2. route = [0] * (MAX+1) #1차원 리스트(그전->다음)
'''

start, goal = map(int, input().split())
MAX = 100000
from collections import deque
answer = [0] * (MAX+1) # +visited 역할
routes = [0] * (MAX+1) #1차원 리스트(그전->다음)

def bfs(start):
    q = deque([start])
    answer[start] = 1 # visited 역할 수행하는 대신에 모든 값이 1 증가한다.
    while q:
        v = q.popleft()
        # 위로
        floor = v + 1
        if floor <= MAX and not answer[floor]:
            q.append(floor)
            answer[floor] = answer[v] + 1
            routes[floor] = v
        # 아래로
        floor = v - 1
        if floor >= 0 and not answer[floor]:
            q.append(floor)
            answer[floor] = answer[v] + 1
            routes[floor] = v
        # 순간이동
        floor = 2*v
        if floor <= MAX and not answer[floor]:
            q.append(floor)
            answer[floor] = answer[v] + 1 
            routes[floor] = v 

def find_route(goal, start):
    answer = []
    path = goal
    while path != start:
        answer.append(path)
        path = routes[path]
    answer.append(start)
    return answer


#실행
bfs(start)
#출력
print(answer[goal] - 1) #visited 안 쓴 댓가
route = find_route(goal, start)
print(*route[::-1])

'''
from 1697. 숨바꼭질
감상 : 리스트에 하나의 기록을 새기니까 이쪽도 하나의 기록을 새기는 방법을 모색하자.
그리고 머리를 쓰자.
print(*list) 너무 유용한 것
'''