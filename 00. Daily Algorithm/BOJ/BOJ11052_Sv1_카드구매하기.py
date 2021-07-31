'''
레인보우 칼라?
검띠 빨띠 파띠 초띠 흰띠 태권도?
내가 모르는 뭔가 있는거 같은데

0개 산다 > N개 산다까지 가장 효율이 나쁜것만 골라사면 된다. 바텀 업!
'''
import sys
input = sys.stdin.readline

N = int(input())
prices = list(map(int, input().split()))

dp = [0] * (N+1)

for i in range(1,N+1):
    for j in range(i):
        dp[i] = max(dp[i], dp[i-(j+1)] + prices[j])

print(dp[-1])

'''
힌트에 카드 자랑 무엇
'''