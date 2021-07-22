'''
F : 건물 최대 층 수
S : 현재 층 
G : 목표 층
U : 위로 x칸 이동
D : 아래로 x칸 이동
감상 : 변수 너무 많지 않슴까. 
위에 있으면 U 연타하고 D 조정, 아래있으면 D 연타하면 되는거 아닌가 싶은데...
그런 간단한 문제가 아니겠지
키워드 : BFS! BFS!
생각 : 그니까 BFS 없이 풀어보자.
'''

F, S, G, U, D = map(int, input().split())

from collections import deque
answer = [0] * (F + 1) #visited를 겸한다.

def bfs(start):
    q = deque([start])
    answer[start] = 1 # visited 안쓰는 대신에 모든 값이 1 증가한다.
    while q:
        v = q.popleft()
        # 위로
        floor = v + U
        if floor <= F and not answer[floor]:
            q.append(floor)
            answer[floor] = answer[v] + 1
        # 아래로
        floor = v - D
        if floor > 0 and not answer[floor]:
            q.append(floor)
            answer[floor] = answer[v] + 1

bfs(S)
if not answer[G]:
    print('use the stairs')
else:
    print(answer[G] - 1) #visited 안 쓴 댓가





'''
1차 도전 : 시간 초과
F, S, G, U, D = map(int, input().split())

#이동 거리
dist = G - S
answer = 0

#올라가는것과 내려가는 것
import math
if dist%(math.gcd(U,D))==0 and U!=0 and D!=0:
    # 파이썬 스왑으로 건물 뒤집기
    if dist < 0:
        dist = abs(dist)
        U, D = D, U 
    #1차적으로 시간 절약
        answer = answer + dist // U
        dist = dist - U * answer
    #세부 조정
    while dist!=0:
        if dist > 0:
            if S + U <= F:
                answer = answer + 1
                S = S + U
                dist = dist - U
            elif S - D > 0:
                answer = answer + 1
                S = S - D
                dist = dist + D
            else:
                answer = 'use the stairs'
                break
        else:
            if S - D > 0:
                answer = answer + 1
                S = S - D
                dist = dist + D
            elif S + U <= F:
                answer = answer + 1
                S = S + U
                dist = dist - U                  
            else:
                answer = 'use the stairs'
                break
    print(answer)
else:
    print('use the stairs')
'''

'''
1차 감상: 네 시간 초과.
층이 최대 100만층 파이썬 연산횟수 1초 2천만이면
U : 104009 D : 11 이런거에 약할거 같았음 ㄲㄲ
시키는대로 BFS 씁시다. 하는김에 아까 했던 것도 반성점 살려서 ㄱㄱ
'''