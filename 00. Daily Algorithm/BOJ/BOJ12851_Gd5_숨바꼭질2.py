'''
감상 : 갑자기 분위기 순간이동
'''

start, goal = map(int, input().split())
MAX = 100000
from collections import deque
answer = [0] * (MAX+1) # +visited 역할
route = [0] * (MAX+1) # 그곳에 갈 수 있는 최단 루트 수

def bfs(start):
    q = deque([start])
    answer[start] = 1 # visited 역할 수행하는 대신에 모든 값이 1 증가한다.
    route[start] = 1
    while q:
        v = q.popleft()
        # 위로
        floor = v + 1
        if floor <= MAX and not answer[floor]:
            q.append(floor)
            answer[floor] = answer[v] + 1
            route[floor] = route[v]
        elif floor <= MAX and answer[floor] == (answer[v] + 1):
            route[floor] = route[floor] + route[v]
        # 아래로
        floor = v - 1
        if floor >= 0 and not answer[floor]:
            q.append(floor)
            answer[floor] = answer[v] + 1
            route[floor] = route[v]
        elif floor >= 0 and answer[floor] == (answer[v] + 1):
            route[floor] = route[floor] + route[v]
        # 순간이동
        floor = 2*v
        if floor <= MAX and not answer[floor]:
            q.append(floor)
            answer[floor] = answer[v] + 1
            route[floor] = route[v]
        elif floor <= MAX and answer[floor] == (answer[v] + 1):
            route[floor] = route[floor] + route[v]

bfs(start)
print(answer[goal] - 1) #visited 안 쓴 댓가
print(route[goal])

'''
from 1697. 숨바꼭질에 route 추가
'''