'''
기존 RGB 거리에 1과 N번의 관계성이 추가 되었다.
스타트를 기록한것까지해서 9번 돌리면 되지 않을까
dp를 추가해서 메모리 4배 ㄱㄱ
'''
import sys
input = sys.stdin.readline

N = int(input())
price = []

for _ in range(N):
    price.append(list(map(int, input().split())))

dp = [[0]*N for _ in range(9)]

# 상수 필요. 최대값.
INF = 1000*1000 + 1

# 스타트 R
dp[0][0] = price[0][0]
dp[1][0] = price[0][0]
dp[2][0] = price[0][0]
dp[0][1] = INF  # 접근 금지
dp[1][1] = price[0][0] + price[1][1]
dp[2][1] = price[0][0] + price[1][2]

for i in range(2,N):
    dp[0][i] = min(dp[1][i-1], dp[2][i-1]) + price[i][0]  #현재 R
    dp[1][i] = min(dp[0][i-1], dp[2][i-1]) + price[i][1]  #현재 G
    dp[2][i] = min(dp[0][i-1], dp[1][i-1]) + price[i][2]  #현재 B

# 스타트 G
dp[3][0] = price[0][1]
dp[4][0] = price[0][1]
dp[5][0] = price[0][1]
dp[3][1] = price[0][1] + price[1][0]
dp[4][1] = INF  # 접근 금지
dp[5][1] = price[0][1] + price[1][2]
for i in range(2,N):
    dp[3][i] = min(dp[4][i-1], dp[5][i-1]) + price[i][0]  #현재 R
    dp[4][i] = min(dp[3][i-1], dp[5][i-1]) + price[i][1]  #현재 G
    dp[5][i] = min(dp[3][i-1], dp[4][i-1]) + price[i][2]  #현재 B

# 스타트 B
dp[6][0] = price[0][2]
dp[7][0] = price[0][2]
dp[8][0] = price[0][2]
dp[6][1] = price[0][2] + price[1][0]
dp[7][1] = price[0][2] + price[1][1]
dp[8][1] = INF  # 접근 금지
for i in range(2,N):
    dp[6][i] = min(dp[7][i-1], dp[8][i-1]) + price[i][0]  #현재 R
    dp[7][i] = min(dp[6][i-1], dp[8][i-1]) + price[i][1]  #현재 G
    dp[8][i] = min(dp[6][i-1], dp[7][i-1]) + price[i][2]  #현재 B

# 스타트와 종착점 동일 (한계 알기 쉽게 계산 X)
dp[0][N-1] = INF
dp[4][N-1] = INF
dp[8][N-1] = INF
answer = INF

# zip 쓰면 스타일리쉬하겠지만 속도는 이쪽이 빠를듯.
# 근데 애초에 2차원 배열 방향 행과 열이 달랐으면 이렇게 할 필요도 없었다.
for i in range(9):
    answer = min(answer, dp[i][N-1])

# print(dp)
print(answer)

'''
하고보니까 드는 느낌인데
이거보다 똑똑한 풀이 절대로 있었을거 같음
'''