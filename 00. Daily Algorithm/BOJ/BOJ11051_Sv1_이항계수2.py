'''
이항 계수 시리즈가 많다. 일단은 방치.
feat. https://velog.io/@stripe2933/series/acmicpc-binom-coeff
'''
# 전처리
import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)  # pypy는 재귀에 약하다고 한다. 헤.

# 사용할 상수
MOD = 10007  # 최대 나눌 수

# dp용 함수
def comb(n, k):
    if n == 1 or k == 0 or k == n:
        return 1

    if dp[n][k] == 0:
        dp[n][k] = ( comb(n-1, k-1) + comb(n-1, k) ) % MOD  # 이 단계에서 합친걸 10007 나누면 메모리 절약 가능
    return dp[n][k]


# nCk
N, K = map(int, input().split())

dp = [[0] * (K+1) for _ in range(N+1)]

print(comb(N, K) % MOD)


'''
시간 복잡도 O(n^2)

이항계수 1은 두고 왔다. 이 싸움에 따라올 수 있을것 같지 않아.
아는 문제 dp하는거잖아 하고 넘어가고 끝날수도 했지만,
블로그에서 차근차근 공부하니 pypy가 재귀에 약하다는 엄청 실전적인 공부를 하였다. 
블로그가 양이 빈약하다는거지 이렇게 딱 맞아 떨어지면 공부할 것도 많은것 같음.
'''

'''
<이항계수 리스트 정리>
BOJ11051_Sv1_이항계수2.py
BOJ11401_Gd1_이항계수3.py
BOJ13977_Gd1_이항계수와쿼리.py
BOJ11402_Pt5_이항계수4.py
BOJ11439_Pt4_이항계수5.py
BOJ14854_Dm1_이항계수6.py
'''