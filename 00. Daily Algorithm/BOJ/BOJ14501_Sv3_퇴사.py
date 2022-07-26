'''
dp인건 확실한데 몇 줄 나오냐가 문제긴 하네
'''
import sys
input = sys.stdin.readline

N = int(input())
tasks = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if i + tasks[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], tasks[i][1] + dp[i + tasks[i][0]])
    
print(dp[0])

'''
뒤에서 부터 확인한다는 생각을 못해본건 솔직히 내가 요즘 감 잃었다는 느낌이긴 하네
'''