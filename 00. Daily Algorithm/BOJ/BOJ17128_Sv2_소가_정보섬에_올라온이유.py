'''
소 그림 귀엽
dp 적는데 N번
하나 바뀔때마다 4개씩 바뀌는데 그게 Q번
여유!
'''

import sys
input = sys.stdin.readline

# 소 마리 수, 장난질 횟수
N, M = map(int, input().split())

cows = list(map(int, input().split()))
cows.append(cows[0])
cows.append(cows[1])
cows.append(cows[2])

tricks = list(map(int, input().split()))

# N차원 배열
dp = [0]*N

for i in range(N):
    dp[i] = cows[i] * cows[i+1] * cows[i+2] * cows[i+3]    

# 장난 좀 쳐 볼까? (소 5마리 이상)

# for trick in tricks:
#     trick = trick - 1
#     dp[(trick - 3) % N] = -dp[(trick - 3) % N] 
#     dp[(trick - 2) % N] = -dp[(trick - 2) % N] 
#     dp[(trick - 1) % N] = -dp[(trick - 1) % N] 
#     dp[trick] = -dp[trick] 
#     # print(dp)
#     print(sum(dp))



# 좀 더 빠르게
sum = sum(dp)
for trick in tricks:
    trick = trick - 1
    dp[(trick - 3) % N] = -dp[(trick - 3) % N] 
    dp[(trick - 2) % N] = -dp[(trick - 2) % N] 
    dp[(trick - 1) % N] = -dp[(trick - 1) % N] 
    dp[trick] = -dp[trick] 
    sum = sum + 2 * dp[(trick - 3) % N]
    sum = sum + 2 * dp[(trick - 2) % N]
    sum = sum + 2 * dp[(trick - 1) % N]
    sum = sum + 2 * dp[trick]
    print(sum)