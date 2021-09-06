'''
DP
선수를 만나서
너를 흑에 넣었을때의 전력과 남은 코스트
너를 백에 넣었을때의 전력과 남은 코스트
너를 안 넣었을때의 전력과 코스트
를 쭉 계산해주면 된다.
뭔가 조조전 하고 싶다.
'''
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

dp = [[[0]*17 for _ in range(17)] for _ in range(n+1)]
 
for i in range(n):
    for w in range(16): 
        for b in range(16):
            # 백 / 흑 / 미선택
            # print('h', dp[i+1][w+1][b] ,dp[i+1][w+1][b], dp[i][w][b],powers[i][0])
            if w+1 <= 15:
            	dp[i+1][w+1][b] = max(dp[i+1][w+1][b], dp[i][w][b] + powers[i][0])
            if b+1 <= 15:
            	dp[i+1][w][b+1] = max(dp[i+1][w][b+1], dp[i][w][b] + powers[i][1])
            dp[i+1][w][b] = max(dp[i+1][w][b], dp[i][w][b])
 
#print(dp[n])
print(dp[n][15][15])

'''
w와 b를 15까지 돌리면 두개가 다 15가 되는 경우의 수가 안나온다. 
그래서 16까지 돌리고, 그랬더니 dp 사이즈 커져서 17이 되었다. 뭔가 어중간.
'''