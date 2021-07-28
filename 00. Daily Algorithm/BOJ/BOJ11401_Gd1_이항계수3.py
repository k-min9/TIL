'''
feat. https://velog.io/@stripe2933/series/acmicpc-binom-coeff
페르마의 소정리 : p가 소수니까 a^(p-1) 모듈러 p는 1이다. 
활용 요점은 따라서, a의 역수와 a의 1000000005 은 모듈러 1000000007 값이 같다는 것.

그 다음은 나누기 싫은 분모를 분자로 바꾸면 된다.
nCr = n!/(r!(n-r)!) % p
-> A = n!, B = (r!(n-r)!)
-> (A*B^(-1)) % p
-> ((A % p)*(B^(-1) % p)) % p
-> (A*B^(p-2)) % p << 여기 페르마

빠르게 제곱하는 법은 덤
'''
# 전처리
import sys
input = sys.stdin.readline


# 상수
MOD = 1000000007

# 빠른 거듭제곱 계산(재귀 >> dp로 더 좋아질 여지 있음)
def fast_pow(n, k, m):
    if k == 1:
        return n
    pow_half = pow(n, k//2, m)
    if k % 2 == 0:
        return (pow_half ** 2) % m
    else:
        return (pow_half ** 2 * n) % m

# 역원 구하기
def inverse(n):
    return pow(factorial[n], MOD-2, MOD)

# 입력
N, K = map(int, input().split())

# 반복형 팩토리얼 세팅
factorial = [1] * (N+1)
for idx in range(2, N+1):
    factorial[idx] = (factorial[idx-1] * idx) % MOD


print(factorial[N] * inverse(N-K) * inverse(K) % MOD)