'''
감상 : 그 시점에 만나야한다. 그게 어렵다.
'''

start, goal = map(int, input().split())
MAX = 500000
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

ans = MAX #갱신되는 정답
flag = False # 답을 찾음
i = 0
while(True):
    goal = goal + i
    if goal >= MAX:
        break 

    tmp = answer[goal] - 1 # 수빈이 도착 시간 (동생 도착시간 = i)

    if tmp > i and (tmp-i)%4 == 0: # 동생이 먼저 도착해서 대기
        flag = True
        tmp = max(tmp, i)
    if tmp <= i and (i-tmp)%2 == 0: #수빈이 먼저 도착해서 대기
        flag = True
        tmp = max(tmp, i)

    if ans > tmp:
        ans = tmp
    i = i + 1


if flag:
    print(ans)
else:
    print('-1')


'''
from 1697. 숨바꼭질
1차. 못 찾는 경우의 설정을 안함
2차. 지연해서 만나는게 tmp = max(tmp,i)가 아니다 좀 더 이상하게 늦게 올 수 있음
좀 더 고민하고 성장한 다음에 리트라이하는걸로!
'''