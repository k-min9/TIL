'''
문제 처음봤을때는 완전탐색인가 했는데 이 M이랑 P면 최악의 견적 = 10^50이므로 그렇게 풀면 아웃
이거 그리디로 풀리나...?
일단 답이 50자리가 넘어가서 다른 언어는 오버플로우가 걸릴 수 있으나 그걸 고려해도 되지 않는게 파이썬의 장점
'''
import sys
input = sys.stdin.readline

# 자릿수, 가격들, 보유 금액
N = int(input())
costs = list(map(int, input().split()))
M = int(input())

# 이건 그냥 탑 다운 DP로 해야 말이 됨 (그래야 최고 자릿수냐 자리수 갯수냐 판단이 되니까)
dp = [0]*(M+1)
for i in range(N-1, -1, -1):
    for j in range(costs[i], M+1):
        dp[j] = max(dp[j], dp[j-costs[i]]*10+i)

print(dp[M])

'''
답은 그리디가 아니라 DP였다...
그리디로 풀릴 법도 한데 내가 못 품...
'''