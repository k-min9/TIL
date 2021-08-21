'''
한번에 쓸 수 있는 웍이 2개
N이 1000 M이 10000
'''

import sys
input = sys.stdin.readline
INF = 10001

# 주문 짜장면(target), 웍의 개수(중복가능)
N, M = map(int, input().strip().split())
pans = list(map(int, input().strip().split()))
pans2 = set()
for i in range(M):
    for j in range(i+1,M):
        # M을 N으로 규격 맞추기(+중복 제거)
        new = pans[i] + pans[j]
        if new <= N:
            pans2.add(new)
    # 한 손 장비
    if pans[i] <= N:
        pans2.add(pans[i])

print(pans2)

dp = [INF]*(N+1)
dp[0] = 0

for i in range(1,N+1):
    for pan in pans2:
        if pan <= i:
            dp[i] = min(dp[i], dp[i - pan] + 1)
print(dp)

if dp[N] >= INF:
    print(-1)
else:
    print(dp[-1])

'''
반성점 : 
1. pans2 조립시 j를 i까지 조립하면 한손장비를 따로 안챙겨도 챙겨진다.
2. pans2를 sort하고 루프돌린 후 넘는 순간 break 해버리면 집어넣을때 N보다 큰지 계산할필요도 없고, i가 낮을때는 훨씬 빨라진다.
2-1. 물론 sort는 NlogN이니까 신중히!(여기서는 M이 N보다 1/10이니까 무조건 하는게 이득이다.)
'''