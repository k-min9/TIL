'''
BOJ1018 에서 체스판 색칠하게 하고, 
다음문제에서 prefix sum 을 배치한건 인간의 악의가 느껴졌다.
그래서 말로만 듣던 counter 라이브러리 성능 조사를 하기로 했다.(?)
아 몰랑 일단 해볼꺼야.
'''
import sys
input = sys.stdin.readline

# from collections import Counter

# 가로 N, 세로 M, 조사구역 수 K
M,N = map(int,input().split()) 
K = int(input())
maps = []

for _ in range(M):
    maps.append(input().rstrip())

# 1차 시도 : 네. 시간 초과. 알고 있었다구
# for _ in range(K):
#     u, l, d, r = map(int, input().split())
#     cnt = Counter()
#     for i in range(u-1,d):
#         cnt = cnt + Counter(maps[i][l-1:r])
#     print(cnt['J'], cnt['O'], cnt['I'])

# 그래도 꺼낸거 아까우니까 마저 쓰자.

# 2차 시도 : 이유는 모르겠는데 또 시간 초과. 카운터랑 딕셔너리 당분간 봉인할 듯
# dp = [[Counter()]*(N+1) for _ in range(M+1)]

# for i in range(1,M+1):
#     for j in range(1,N+1):
#         dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + Counter(maps[i-1][j-1])


# for _ in range(K):
#     i1, j1, i2, j2 = map(int, input().split())
#     i1 = i1 - 1
#     j1 = j1 - 1
#     cnt = dp[i2][j2] + dp[i1][j1] - dp[i1][j2] - dp[i2][j1] 
#     print(cnt['J'], cnt['O'], cnt['I'])

#dp = [[[0]*3]*(N+1) for _ in range(M+1)] 주소 복사의 폐해를 직접 맛 볼 수 있었다.
dp = [[[0]*3 for _ in range(N+1)] for _ in range(M+1)]

for i in range(1,M+1):
    for j in range(1,N+1):
        for k in range(3): 
            new = 0
            if k == 0 and maps[i-1][j-1] == 'J':
                new = 1
            elif k == 1 and maps[i-1][j-1] == 'O':
                new = 1
            elif k == 2 and maps[i-1][j-1] == 'I':
                new = 1
            dp[i][j][k] = dp[i][j-1][k] + dp[i-1][j][k] - dp[i-1][j-1][k] + new

for _ in range(K):
    i1, j1, i2, j2 = map(int, input().split())
    i1 = i1 - 1
    j1 = j1 - 1
    answer = [0,0,0]
    for k in range(3):
        answer[k] = dp[i2][j2][k] + dp[i1][j1][k] - dp[i1][j2][k] - dp[i2][j1][k]

    print(answer[0], answer[1], answer[2])


'''
python3 : 4592ms > pypy : 660ms 속도 차이 무엇
참고로 2차 시도 코드도 pypy는 3204ms로 통과한다. 메모리는 약 2.5배
'''