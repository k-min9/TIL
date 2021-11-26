'''
그냥 쭉 계산해도 될것같은데
'''
N = int(input())

num = 1
for i in range(1, N+1):
    num *= i
    num %= 1000000000000
    while num % 10 == 0:
        num /= 10
print(int(num % 10))