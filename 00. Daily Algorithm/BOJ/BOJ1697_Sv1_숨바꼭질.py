'''
감상 : 갑자기 분위기 순간이동
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
        # 순간이동
        floor = 2*v
        if floor <= MAX and not answer[floor]:
            q.append(floor)
            answer[floor] = answer[v] + 1       

bfs(start)
print(answer[goal] - 1) #visited 안 쓴 댓가

'''
feat 5014.스타트링크
'''