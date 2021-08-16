'''
RGB 거리 N색 버전 >> Failed
'''
import sys
input = sys.stdin.readline

# 가위바위보 종류, 필요 승 수
N,K = map(int,sys.stdin.readline().split())

# 가위바위보 상성
power_graph = []
for _ in range(N):
    power_graph.append(list(map(int,sys.stdin.readline().split())))

# 경쟁자 정보 입력
player2 = list(map(int,sys.stdin.readline().split()))
player3 = list(map(int,sys.stdin.readline().split()))

# 그 전에 낸 걸 제외하고 최고 DP(그리디)
def vs_p1(i, p1):
    # 최대 승수, 최소 패수
    ret1 = 0
    ret2 = 41
    ret3 = 41
    for k in range(N):
        if k != p1:
            if ret1 <= dp[i][k][0]:
                ret1 = max(ret1, dp[i][k][0])
                ret2 = min(ret2, dp[i][k][1])
                ret3 = min(ret3, dp[i][k][2])

    if ret1 < K:
        return ret1, ret2, ret3
    elif ret2 >= K or ret3>= K:
        print('1', ret2, ret3)
    else:
        print('0', ret2, ret3)

# 이겨야 승점이 쌓임
def vs_p2(p1, p2):
    if power_graph[p1-1][p2-1] == 2:
        return 1
    return 0

# 비겨도 승점이 쌓임
def vs_p3(p1, p3):
    if power_graph[p1-1][p3-1] == 2 or power_graph[p1-1][p3-1] == 1:
        return 1
    return 0

# 나의 승수만 입력 >> 모두의 승수를 입력
dp = [[[0,0,0] for _ in range(N)] for _ in range(41)]

# 승부다!
try:
    for i in range(20):
        # vs 경희
        for j in range(N):
            dp[2*i+1][j][0] = vs_p1(2*i, j)[0] + vs_p2(j,player2[i])
            dp[2*i+1][j][1] = vs_p1(2*i, j)[1] + (1-vs_p2(j,player2[i]))

        # 승리 체크
        vs_p1(2*i+1, j)

        # 경희 vs 민호
        for j in range(N):
            dp[2*i+1][j][1] = dp[2*i+1][j][1] + vs_p2(player2[i], player3[i])
            dp[2*i+1][j][2] = dp[2*i][j][2] + (1-vs_p2(player2[i], player3[i]))

        # vs 민호
        for j in range(N):
            dp[2*i+2][j][0] = vs_p1(2*i+1, j)[0] + vs_p2(j,player2[i])
            dp[2*i+2][j][1] = vs_p1(2*i+1, j)[1] 
            dp[2*i+2][j][2] = vs_p1(2*i+1, j)[2] + (1-vs_p2(j,player2[i]))
    print(0)
except:
    pass

for i in range(41):
    print(*dp[i])