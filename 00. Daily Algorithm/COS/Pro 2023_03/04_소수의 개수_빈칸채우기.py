'''
빈칸채우기
'''

def func_a(n):
    if n == 1:
        return False
    i = 2
    while i *i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def func_b(a, b):
    cnt = 0
    for i in range(a, b + 1):
        if func_a(i):
            cnt += 1
    return cnt

def solution(a, b):
    answer = func_b(a, b)
    return answer