'''
브론즈 아니고?
'''
def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a*b//gcd(a,b))

'''
오늘의 교훈은 자작 오버라이드 gcd가 조금 더 빠르다는거다.
'''