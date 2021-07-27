'''
예제가 없으면 이해도 제대로 못했을 자신이 있다.
도형은 잊자. 점과 벡터?만 보자.
'''
'''
방향 0부터 세대별 이동방향
0
01
0121 << 1. 그전 세대 01을 뒤집어서 10 2. 1씩 더해서 21 3. 01+21
01212321
기존거 + (기존거 + 1)%4
'''
# 기본 전처리
import sys
input = sys.stdin.readline
from collections import deque  # 선입선출

# 꼭지점 set와 이동 명령 0 1 2 3
vertexs = set()
move = ((1,0),(0,-1),(-1,0),(0,1))

curveNum = int(input())
for _ in range(curveNum):
    # 시작점 x,y, 시작 방향, 세대
    x, y, d, g = map(int, input().split())
    now = (x, y)
    vertexs.add(now)

    # 명령 순서대로 탑재(de큐)
    orders = deque([d])
    for _ in range(g):
        orderNew = reversed(orders)  # 연산 낭비
        orderNew = list(map(lambda x: (x+1)%4, orderNew))  # 오 이게 되네
        orders.extend(orderNew)

    # 명령대로 일해라
    while(orders):
        d = orders.popleft()
        now = (now[0]+move[d][0], now[1]+move[d][1])
        #print('go', d, now)
        vertexs.add(now)

# 꼭지점 다 만들었으니 사각형 찾자
count = 0
for i in range(100):
    for j in range(100):
        if (i,j) in vertexs and (i+1,j) in vertexs and (i,j+1) in vertexs and (i+1,j+1) in vertexs:
            count = count + 1

#길었다...
print(count)


'''
100 * 100이라 사각형 저렇게 찾았는데 원래 찾는 법 따로 있겠지... 으어어
'''