'''
순간 무슨 소리인가 할 수 있지만,
표 그리면 엄청 단순한 구현 문제임을 알 수 있다.
M에서 N과 M의 최대공약수를 빼면 끝!
'''
import sys
input = sys.stdin.readline

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

N, M = map(int, input().split())
print(M - gcd(N, M))