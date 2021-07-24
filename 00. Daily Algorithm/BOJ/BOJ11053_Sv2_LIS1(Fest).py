'''
<가장 긴 증가하는 부분 수열(Longest Increasing Subsequence aka.LIS) 축제 on 2021.07.24>
이거 할 때가 아닌거 같지만 하고 싶을때 하는거지!
'''

import sys
input = sys.stdin.readline

def getDP_LIS(N, seq ,dp):
    for i in range(N):
        for j in range(i):
            if seq[j] < seq[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp


# 입력
N = int(input()) # 수열 크기
seq = list(map(int,input().split())) #수열

# DP
dp = [1]*N #LIS적용

dp = getDP_LIS(N, seq, dp)

#출력
print(max(dp))

'''
<축제 리스트 정리>
BOJ11054_Gd3_LIS_바이토닉.py << 여기서 시작
BOJ11053_Sv2_LIS(Fest).py
BOJ11053_Sv2_LIS.py
BOJ11722_Sv2_LDS.py
BOJ11055_Sv2_LIS_Sum.py
BOJ12015_Gd2_LIS2.py
BOJ12738_Gd2_LIS3.py
BOJ14002_Gd4_LIS4.py
BOJ14003_Pt5_LIS5.py
BOJ17411_Pt1_LIS6.py

<보류>
BOJ16161_Gd1_LIS_펠린드롬.py
BOJ18837_Dm3_LIS_K.py
BOJ18838_Dm5_LIS_k.py
BOJ18892_Gd1_LIS_ks.py
'''