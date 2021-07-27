'''
dp, 명확한 전 단계가 있지만 인덱스 기록을 해보자
'''

# 기본 전처리
import sys
input = sys.stdin.readline

# 빠른 입력
N = int(input())
map = input().rstrip()

#dp 준비 끝
INF = 1e9
dp = [INF]*N
dp[0] = 0

for i in range(1, N):
    #인덱스 세팅
    if map[i] == 'B':
        idxStr = 'J'
    elif map[i] == 'O':
        idxStr = 'B'
    else:
        idxStr = 'O'
    #캐싱
    for j in range(i):
        if map[j] == idxStr:    
            dp[i] = min(dp[j] + (i - j) ** 2, dp[i])

if dp[N-1] != INF:
    print(dp[N-1])
else:
    print(-1)



'''
조금 세련되게 쓰려다가 하드코딩만도 못한 코딩을 하는 전형적인 예시
차라리 인풋을 0 1 2로 변환하면서 받았으면 이뻤을뻔했다.

>> 아니 진짜 너무 못생겨서 하드코딩 다이어트 했다. 이제 좀 이쁘네 무식한게 짱이다.
'''