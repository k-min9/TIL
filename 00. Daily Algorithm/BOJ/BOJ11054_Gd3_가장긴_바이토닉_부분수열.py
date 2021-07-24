'''
감상 : 아는 문제
접근 : 가장 긴 증가하는 부분수열(LIS)과 그 reverse 버전 합치면 끝
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
dp1 = [1]*N #LIS적용
dp2 = [1]*N #리버스 하고 LIS적용

#오름차순
dp1 = getDP_LIS(N, seq, dp1)
#내림차순
seq.reverse()
dp2 = getDP_LIS(N, seq, dp2)
dp2.reverse()

#출력
answer = []
for i in range(N):
    answer.append(dp1[i]+dp2[i])


print(max(answer)-1)

'''
원래라면 내림차수 함수 따로 만들어야 함, 
근데 이렇게만 해도 구동법 알고, 애초에 아는 문제니까 점검만 하고 넘어감.
'''