'''
0-1 배낭 문제인데 카카오 시험보고 조금 마음이 꺾였어...
변수가 둘 -> dp[주문][버거][감튀]
'''

import sys
input = sys.stdin.readline

# 주문 수, 버거수, 감튀 수
N, M, K = map(int, input().split())
orders = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0]*(K+1) for _ in range(M+1)] for _ in range(N+1)]


for n in range(1,N+1):
    bur, fri = orders[n-1]
    for m in range(1, M+1):
        for k in range(1, K+1):
            # 오더 체크
            if bur<=m and fri<=k:
                dp[n][m][k] = max(dp[n-1][m-bur][k-fri] + 1, dp[n-1][m][k])
            else:
                dp[n][m][k] = dp[n-1][m][k]

print(dp[n][m][k])

'''
이렇게 좋은데 중간과정 출력에 막히다니...
높은 점수 순 선택 출력이라도 보고 싶으면 카카오2021블라인드 9월차의 4번 틀린 풀이 참조 ㅠ

추가 - 이런 3중문 쓰면 pypy가 빠르다 약 20배 정도 빨랐음
'''