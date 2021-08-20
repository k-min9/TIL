'''
에이 냅색이네 하고 지나가려는 순간 초등부 문제란걸 봐버렸다.
dp[현재도시][현재시간] = dp[이전도시][이전시간] + 모금액
'''


import sys
input = sys.stdin.readline
N, K = map(int,input().split())
dp = [[0]*(K+1) for _ in range(N+1)]
infos = [list(map(int,input().split())) for _ in range(N)]

time1, price1, time2, price2 = infos[0]
if time1<=K:
    dp[1][time1] = price1
if time2<=K:
    dp[1][time2] = max(dp[1][time2], price2)

for i in range(1,N):
    time1, price1, time2, price2 = infos[i]
    for j in range(K):
        if dp[i][j] and j+time1<=K:
            dp[i+1][j+time1] = max(dp[i+1][j+time1], dp[i][j] + price1)
        if dp[i][j] and j+time2<=K:
            dp[i+1][j+time2] = max(dp[i+1][j+time2], dp[i][j] + price2)
print(max(dp[-1]))


'''
>> 1차 시도 : 시간 초과
import sys
input = sys.stdin.readline


# 도시, 시간
N, K = map(int, input().split())
dp = [[] for _ in range(N+1)]
dp[0].append([0,0])

for i in range(N-1):
    # 1: 도보 2: 자전거
    time1, price1, time2, price2 = map(int, input().split())
    for time, price in dp[i]:
        if time+time1 <= K:
            dp[i+1].append([time+time1, price+price1])
        if time+time2 <= K:
            dp[i+1].append([time+time2, price+price2])

# 출력
answer = 0
time1, price1, time2, price2 = map(int, input().split())
for time, price in dp[N-1]:
    if time+time1 <= K:
        answer = max(answer, price+price1)
    if time+time2 <= K:
        answer = max(answer, price+price2)

print(answer)
'''

# 오늘의 교훈 : 냅색은 확실한 O(NK) 풀이로 풀자. 오히려 빠르다.