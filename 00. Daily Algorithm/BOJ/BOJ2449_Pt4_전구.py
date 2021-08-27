'''
16157 블로그와 흡사한 문제
차이점 : 처음에 하나 색칠하고 가는게 없어서 + 1 없어져도 됨
3색이 아니라 k색(최대 9)
'''

n, m = map(int, input().split())
s = list(map(lambda x: int(x) - 1, input().split()))

dp = [[[-1]*m for j in range(n)] for i in range(n)]
# [i..j] in background color k
def getdp(i, j, k):
    if i > j: return 0
    if dp[i][j][k] != -1: return dp[i][j][k]
    if s[i] == k: return getdp(i+1, j, k)
    if s[j] == k: return getdp(i, j-1, k)
    ans = n
    for mid in range(i, j+1):
        ans = min(ans, 1 + getdp(i+1, mid, s[i]) + getdp(mid+1, j, k))
    dp[i][j][k] = ans
    return ans

print(0 + min(getdp(0, n-1, k) for k in range(m)))


# 인상 깊었던 풀이
# import sys

# N, K = list(map(int, input().split()))
# datas = list(map(int, input().split()))

# # 데이터 압축 111222333444222 > 12342
# reData = [ datas[0] ]
# for i, data in enumerate( datas[1:] ):
#     i += 1
#     if data != reData[-1]:
#         reData.append( data )

# datas = reData
# N = len(datas)

# # 
# dp = [[0]*N for i in range(N)]
# for end in range(N):
#     for start in range( end-1, -1, -1 ):
#         dp[start][end] = sys.maxsize
#         for mid in range( start, end ):
#             if datas[start] == datas[mid+1]:
#                 dp[start][end] = min( dp[start][end], dp[start][mid] + dp[mid+1][end] )
#             else:
#                 dp[start][end] = min( dp[start][end], dp[start][mid] + dp[mid+1][end] + 1 )
# print( dp[0][N-1] )