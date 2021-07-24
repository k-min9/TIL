'''
<가장 긴 증가하는 부분 수열(Longest Increasing Subsequence aka.LIS) 축제>
~ on 2021.07.24 from BOJ11053_Sv2_LIS(Fest).py
'''

def getDP_LISSum(N, seq ,dp):
    for i in range(N):
        for j in range(i):
            if seq[j] < seq[i]:
                dp[i] = max(dp[i], dp[j] + seq[i])
    return dp


# 입력
N = int(input()) # 수열 크기
seq = list(map(int,input().split())) #수열

# DP
#dp = [1]*N #LIS적용
dp = [i for i in seq] # 또 하나 배웠네

dp = getDP_LISSum(N, seq, dp)

#출력
print(max(dp))

'''
리스트 복사하는 법 : [i for i in seq]
'''