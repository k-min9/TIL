'''
가장 큰 증가 부분수열 반대버전.
dp 계산으로 그 시점까지 수 중 가장 큰 값
'''
import sys
input = sys.stdin.readline

# 입력
N = int(input())
seq = list(map(int,input().split()))[::-1]

# dp 기본값 : 리스트 복사
dp = seq[:]

# dp
for i in range(N):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j] + seq[i])


#출력
print(max(dp))

'''
11055 할때보다 많은 성장을 느낀다 ㄷㄷㄷ
'''