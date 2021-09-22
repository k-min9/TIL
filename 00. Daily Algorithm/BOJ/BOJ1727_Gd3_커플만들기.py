'''
남자랑 여자랑 순서대로 정렬하고, 선을 이어주면 신발끈 묶이듯이 묶일듯?
dp[i번째남자][j번째 여자]
'''

N, M = map(int,input().split())
man = list(map(int,input().split()))
woman = list(map(int,input().split()))

man.sort()
woman.sort()

dp=[[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        # 묶기
        dp[i][j] = dp[i-1][j-1] + abs(man[i-1]-woman[j-1])
        # 안 묶기 (기존 값 최적화)
        if i > j:
            dp[i][j] = min(dp[i][j], dp[i-1][j])
        elif i < j:
            dp[i][j] = min(dp[i][j], dp[i][j-1])

print(dp[N][M])