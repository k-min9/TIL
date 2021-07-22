'''
감상 : 리얼로 순간이동
접근 : 가볍게 수정했다가 가볍게 틀림
키워드 : 0-1 BFS
'''

start, goal = map(int, input().split())
MAX = 100000
from collections import deque
answer = [0] * (MAX+1) # +visited 역할

def bfs(start):
    q = deque([start])
    answer[start] = 1 # visited 역할 수행하는 대신에 모든 값이 1 증가한다.
    while q:
        v = q.popleft()
        # 순간이동 [먼저 연산해야 한다/ 간선 길이 0]
        floor = 2 * v
        if floor <= MAX and not answer[floor]:
            q.appendleft(floor) #우선순위 올리기
            answer[floor] = answer[v] + 0        
        # 위로
        floor = v + 1
        if floor <= MAX and not answer[floor]:
            q.append(floor)
            answer[floor] = answer[v] + 1
        # 아래로
        floor = v - 1
        if floor >= 0 and not answer[floor]:
            q.append(floor)
            answer[floor] = answer[v] + 1


bfs(start)
print(answer[goal] - 1) #visited 안 쓴 댓가

'''
from 1697. 숨바꼭질에서 순간이동(2*v) 부분 위로 올리고, appenleft로 우선순위 주고, 1->0으로 변경
0-1 BFS 라는 말 처음 들었고 생각 이상으로 당황했다.
'''