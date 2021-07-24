'''
<가장 긴 증가하는 부분 수열(Longest Increasing Subsequence aka.LIS) 축제>
~ on 2021.07.24 from BOJ11053_Sv2_LIS(Fest).py
'''

import sys
input = sys.stdin.readline

def getDP_LDS(N, seq ,dp):
    for i in range(N-1,-1,-1):
        for j in range(N-1,i,-1):
            if seq[j] < seq[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp


# 입력
N = int(input()) # 수열 크기
seq = list(map(int,input().split())) #수열

# DP
dp = [1]*N #LDS적용

dp = getDP_LDS(N, seq, dp)

#출력
print(max(dp))