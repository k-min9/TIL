'''
요약 : N+K-1CK-1를 구하라
숫자가 너무 커서 dp로 파스칼의 삼각형 직접 구축하면서 MOD 절단
'''
import sys
input = sys.stdin.readline

# 상수
MOD = 1000000000

N, K = map(int, input().split())
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(N+1):
    dp[i][1] = 1

for i in range(K+1):
    dp[1][i] = i

for i in range(2, N+1):
    for j in range(2, K+1):
        # nCr = n-1Cr-1 + n-1Cr
        dp[i][j] = (dp[i-1][j]+dp[i][j-1]) % MOD

# for i in range(N+1):
#     print(*dp[i])

print(dp[N][K])

'''
올만에 학생시절로 돌아간 키분...

참고로 하나만 구하면 평범하게 이쪽이 빠르다. 
5배 정도. 메모리도 안먹음

N, K = map(int,input().split())
ans=1
for i in range(min(N, K-1)):
    ans=ans*(N+K-1-i)//(i+1)
print(a%1000000000)

'''
