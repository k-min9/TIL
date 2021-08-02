'''
자신의 공부 시간에 한계가 있다. 라는 말이 너무 울리는데...
dp로 배낭문제긴 한데, 기본 틀을 구글로 리버스 엔지니어링하고 예시 뜯어보기 했다.
'''

import sys
input = sys.stdin.readline

# 최대 공부시간, 과목 수
N, K = map(int,input().split())

# dp
dp = [[0]*(N+1) for _ in range(K+1)]

# 입력
priors = []
times = []
for _ in range(K):
    prior, time = map(int,input().split())
    priors.append(prior)
    times.append(time)
    
# 세로줄 과목 종류, 가로줄 시간 (O(N*K) = 대충 천만)
for i in range(1,K+1):
    for j in range(1,N+1):
        # 과목을 선택한다. 선택하지 않는다.
        #print('1', times[i-1], j)
        if times[i-1] > j:
            dp[i][j] = dp[i-1][j]
            #print('2', i, j, times[i-1], dp[i][j] )
        else:
            dp[i][j] = max(priors[i-1] + dp[i-1][j-times[i-1]], dp[i-1][j])
            #print('3', i, j, dp[i][j])

#print(dp)
print(dp[K][N])

'''
??? Python 시간 초과 튕기고 PyPy 써야되는데요 ???


-- 안튕기게 적는 법 -- 
for i in range(1, k + 1):
    a, b = map(int, input().split())
    for j in range(1, n + 1):
        if j < b:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - b] + a, dp[i - 1][j])

print(dp[-1][n])

>>>> 오우야...
'''