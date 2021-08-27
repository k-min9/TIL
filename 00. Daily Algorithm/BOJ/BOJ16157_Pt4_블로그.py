'''
dp[L][R][color]의 3차원 DP
[L, R)내의 모든 i에 대해 DP(L, i, Color) + DP(i + 1, R, Color)
>>>>> 라고 생각하던 시기가 저에게도 있었습니다. 2449 전구로 가주세요(N이 2배인 200, 색은 3배인 9색)
'''
import sys
input = sys.stdin.readline

# 상수
INF = sys.maxsize

def coloring(l, r, color):
    if l == r:
        # 색칠할 경우 중간에 있음(대국에 영향 없음)
        if colors[l] == color:
            return 0
        else:
            return 1
    # 이러려고 -1 선언
    elif dp[l][r][color] >= 0:
        return dp[l][r][color]

    ret = INF
    for i in range(l,r):
        ret = min(ret, coloring(l, i , color) + coloring(i+1, r, color))

    if not visited[l][r][color]:
        visited[l][r][color] = 1
        for i in range(3):
            if i != color:
                ret = min(ret, coloring(l,r,i) + 1)

    dp[l][r][color] = ret
    return ret

N = int(input())
colors = list()
for s in input().rstrip():
    if s == 'R':
        colors.append(0)
    elif s == 'B':
        colors.append(1)
    else:
        colors.append(2)

dp = [[[-1]*3 for _ in range(N)] for _ in range(N)]
visited = [[[0]*3 for _ in range(N)] for _ in range(N)]

answer = coloring(0,N-1,0)
answer = min(answer, coloring(0,N-1,1))
answer = min(answer, coloring(0,N-1,2))

print(answer + 1)

# ============================
# 깔끔하고 인상깊은 풀이가 있어서 가져왔다.

# n = int(input())
# s = ["RGB".find(c) for c in input()]

# print(s)

# dp = [[[-1]*3 for j in range(n)] for i in range(n)]
# # [i..j] in background color k
# def getdp(i, j, k):
#     if i > j: return 0
#     if dp[i][j][k] != -1: return dp[i][j][k]
#     if s[i] == k: return getdp(i+1, j, k)
#     if s[j] == k: return getdp(i, j-1, k)
#     ans = n
#     for mid in range(i, j+1):
#         ans = min(ans, 1 + getdp(i+1, mid, s[i]) + getdp(mid+1, j, k))
#     dp[i][j][k] = ans
#     return ans

# print(1 + min(getdp(0, n-1, k) for k in range(3)))