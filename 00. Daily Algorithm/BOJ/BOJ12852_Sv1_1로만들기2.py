'''
접근 : dp 바텀업으로 10만까지 쭉 더하면 될 것 같은데
'''
import sys
input = sys.stdin.readline

# 계산 횟수 dp와 그 dp가 어디서 왔는지
dp = [1000001] * 1000001
dp[0] = 0
dp[1] = 0
dp_before = [0] * 1000001


for i in range(2, 1000001):
    if dp[i-1] + 1 < dp[i]:
        dp[i] = dp[i-1] + 1
        dp_before[i] = i-1
    if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
        dp[i] = dp[i//2] + 1
        dp_before[i] = i//2
    if i % 3 == 0 and dp[i//3] + 1 < dp[i]: 
        dp[i] = dp[i//3] + 1
        dp_before[i] = i//3

# 시작
N = int(input())
print(dp[N])
answers = [N]
while N:
    print(N, end=' ')
    N = dp_before[N]
print()

'''
dp_before 부분 출력 안하면 BOJ1463_Sv3_1로만들기
'''