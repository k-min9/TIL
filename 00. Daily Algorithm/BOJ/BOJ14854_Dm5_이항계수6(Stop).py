'''
feat. https://velog.io/@stripe2933/series/acmicpc-binom-coeff
중국인의 나머지 정리 : 
'''

import sys
input = sys.stdin.readline
print = sys.stdout.write

# 초기값을 기준으로 데이터를 순회, 집계함수를 적용, 누적 적용 결과를 반환.
# 속도와 가독성이 올라간다고 한다.
from functools import reduce  
from operator import ge, mul  # operator 곱하기(mul)

# 정수론 : a (mod b)의 모듈러 역수
# 확장 유클리드 알고리즘 feat 유클리드 호제법 : 
# (https://blog.silnex.kr/%EC%A0%9C-5%EA%B0%95-%ED%99%95%EC%9E%A5-%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-function/)
def get_modulo_inverse(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        # 파이써닉한 스왑
        a, b = b, a % b  
        x0, x1 = x1 - q * x0 , x0
    if x1 < 0:
        x1 = x1 + b0
    return x1

# 딕셔너리에 각각 팩토리얼과 역수를 담는다.(dp)
# 작성자 의도 : 이후의 이식 가능성, 범용성을 염두 
# >> 이 문제만 생각하면 factorial, inverse, p_adic_factorial, p_adic_inverse를 37까지 계산하고 시작하는게 훨씬 빠름
factorial = {}
inverse = {}

# nCm % p(소수, 제곱 없음) 구하기
def calc_modulo_prime(n, m, p):
    
    # 사용할 팩토리얼 + dp
    def get_factorial(num):
        if p not in factorial:
            factorial[p] = {0:1, 1:1}
        for idx in range(2, num+1):
            factorial[p][idx] = factorial[p][idx-1] * idx % p  # 데이터 절약 및 우리가 딕셔너리로 관리하는 이유
        return factorial[p][num]
    
    # 사용할 역수 + dp
    def get_inverse(num):
        if p not in inverse:
            inverse[p] = {0:1, 1:1}
        for idx in range(2, num+1):
            inverse[p][idx] = get_modulo_inverse(get_factorial(idx), p)  # 데이터 절약 및 우리가 딕셔너리로 관리하는 이유
        return inverse[p][num]

    choose_prod = 1
    while n != 0 or m!= 0:
        n_digit = n % p
        n = n // p
        m_digit = m % p
        m = m // p

        if n_digit < m_digit:
            choose_prod = 0
            break
        else:
            choose_prod = choose_prod * get_factorial(n_digit) * get_inverse(m_digit) * get_inverse(n_digit-m_digit)
            choose_prod = choose_prod % p

    return choose_prod



'''
아직 더 남았는데 솔직히 개발자 공부라기보다 수학자 공부인거 같아서 일단 여기서 일단락
여기까지만 해도 이항계수 3번은 풀 수 있다. 단 p가 너무 커지면 시간이 늘어지는 타입이므로 그렇게 적합하지는 않음.
'''




'''
나누는 값 소인수 분해 >> 분해한 소수에 따른 나머지 각각 구하기[O((logn)^2)] >> 중국인의 나머지 정리로 합산

유클리드 확장 알고리즘 단순 요약 유클리드 호제법을 거꾸로 
1 ≡ ☆×b + ★×a (mod b) 라면, ★값이 역원(우리가 찾는 값)이다.
'''

'''
결론 : 수학공부??? 똑똑해진건 같은데 최대 수확이 sys.stdout.write일 정도로 지금 당장은 실전성이 너무 없다.
'''