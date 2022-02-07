'''
18290 백트래킹 고도화 >> DP + 비트마스킹 
ㄴ학습완료
'''
n, m, k = map(int,input().split())
grid = [list(map(int,input().split())) for i in range(n)]
INF = 10**7
MASK = (1<<m)-1

dp = [[-INF]*(1<<m) for ch in range(k+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(m):
        new = [[-INF]*(1<<m) for ch in range(k+1)]
        for ch in range(k+1):
            for bit in range(1<<m):
                nbit = (bit<<1)&MASK
                new[ch][nbit] = max(new[ch][nbit], dp[ch][bit])
                if ch == k: continue
                if j>0 and bit&(1 | (1<<(m-1))): continue
                if j==0 and bit&(1<<(m-1)): continue
                nval = dp[ch][bit] + grid[i][j]
                new[ch+1][nbit|1] = max(new[ch+1][nbit|1], nval)
        dp = new
print(max(dp[k]))