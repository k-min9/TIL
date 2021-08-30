import sys
input = sys.stdin.readline

# 유클리드
def gcd(a,b):
    if a<b:
        a, b = b, a
    while a%b:
        a = a%b
        a, b = b, a
    return b

a,b = map(int,input().split())

answer = gcd(a,b)
print(answer)
print(a*b//answer)