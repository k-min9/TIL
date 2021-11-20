'''
소수 문제 = 에라토스테네스의 체
일단 첫자리가 무조건 2,3,5,7인것만 고려해도 연산을 60% 감소시킬 수 있음
'''
import sys
input = sys.stdin.readline

N=int(input())

def isPrime(a):
    for i in range(2, int(a**0.5)+1):
        if(a%i==0):
            return False
    return True

def dfs(num):
    if len(str(num)) == N:
        print(num)  # 출력
    else:
        for i in range(10):
            temp=num*10+i
            if isPrime(temp):
                dfs(temp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)