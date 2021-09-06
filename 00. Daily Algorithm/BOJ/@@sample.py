import sys
input = sys.stdin.readline

# 전투력,  선수 수
powers = list()
n = 0
while True:
    try:
        a, b = map(int, input().split())
        powers.append((a, b))
        n += 1
    except:
        break

# print(powers)

dp = [[0]*16 for _ in range(16)]
 
for i in range(n):
    for w in range(15):
        for b in range(15):
            # 백 / 흑 / 미선택
            # print('h', dp[i+1][w+1][b] ,dp[i+1][w+1][b], dp[i][w][b],powers[i][0])
            if w+1 <= 15:
            	dp[w+1][b] = max(dp[w+1][b], dp[w][b] + powers[i][0])
            if b+1 <= 15:
            	dp[w][b+1] = max(dp[w][b+1], dp[w][b] + powers[i][1])
 
print(dp[15])
print(dp[15][15])