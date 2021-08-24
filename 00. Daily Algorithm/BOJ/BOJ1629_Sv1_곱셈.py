'''
거듭제곱의 분할정복.
제곱 수가 홀수면 (10^5)*(10^5)*10
제곱 수가 짝수면 (10^5)*(10^5)
'''

def my_power(a, b):
    # 재귀 리턴 포인트
    if b == 1:
        return a % C
    else:
        temp = my_power(a, b // 2)
        if b % 2 == 0:
            # 짝수
            return temp * temp % C
        else:
            # 홀수
            return temp * temp * a % C

A, B, C = map(int, input().split())

result = my_power(A, B)
print(result)