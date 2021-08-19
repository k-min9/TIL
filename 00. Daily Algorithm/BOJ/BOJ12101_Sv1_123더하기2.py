'''
접근 : N이 10까지 밖에 안 됨 
= 하고 싶은거 다 해먹어라
= 최악의 케이스로만 돌려라
'''

import sys
input = sys.stdin.readline

# 저는 dp에 리스트를 집어넣겠습니다.
dp = [[] for _ in range(10)]
dp[0].append([1])
dp[1].extend([[1,1],[2]])
dp[2].extend([[1,1,1],[1,2],[2,1],[3]])

# dp 확대범이라고 불러주세요
for i in range(7):
    for x in dp[i]:
        dp[i+3].append(x+[3])
    for x in dp[i+1]:
        dp[i+3].append(x+[2])
    for x in dp[i+2]:
        dp[i+3].append(x+[1])

N, K = map(int, input().split())
if K > len(dp[N-1]):
    print(-1)
else:
    dp[N-1].sort()
    # print(dp[N-1])
    # print(dp[N-1][K-1])
    print('+'.join(map(str,dp[N-1][K-1])))

'''
4까지만 더하래도 10까지 더해서 주는 친절서비스
'''