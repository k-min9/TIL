'''
1차 : dp[i][x][y] : i번째 햄버거 시점에서 첫번째 선배가 얻은 효용(x)과 두번째 선배가 얻은 효용(y) -> 시간초과
2차 : dp[x][y] : x, y효용을 가지는게 가능함
내 효용 = 전체 - x - y  << 얘가 최대가 되면 됨
'''
import sys
input = sys.stdin.readline

N = int(input())
hams = list(map(int, input().split()))
sums = sum(hams)
dp = [[0]*(sums+1) for _ in range(sums+1)]
dp[0][0] = 1

for i in range(N):
    for x in range(sums,-1,-1):
        for y in range(sums,-1,-1):
            if x-hams[i] >= 0:
                dp[x][y] |= dp[x-hams[i]][y]
            if y-hams[i] >= 0:
                dp[x][y] |= dp[x][y-hams[i]]

answer = 0
for x in range(sums+1):
    for y in range(sums+1):
        # 그 효용이 가능한지 선배보다 작은지
        if dp[x][y] and y >= (sums-x-y) and x >= (sums-x-y):
            answer = max(answer, sums-x-y)

print(answer)


