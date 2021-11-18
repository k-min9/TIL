'''
T가 없으면 바로 이렇게 풀었겠지만, 
T가 40이라는 어중간 숫자여서 반복 없애고 dp 계산할까 살짝 고민한 문제
근데 dp야 워낙 많이 풀었으니 이대로 풀어봄
'''
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    zero = 1
    one = 0
    for _ in range(n):
        # 직접 써보면 알 수 있고, 트랜잭션하게 정리
        one, zero = one + zero, one
    print(zero, one)