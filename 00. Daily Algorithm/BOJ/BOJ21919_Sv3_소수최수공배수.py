''''
소수면 전부 곱하면 걍 최소공배수 아닌가??
'''
import sys
input = sys.stdin.readline

# 상수
# MAX = 1000000
# ROOT = MAX**0.5 + 1

# 소수판별
def is_prime(a):
    if a == 1:
        return False
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    return True


input()
nums = list(map(int, input().split()))

answer = 1
for num in nums:
    if is_prime(num):
        answer *= num

if answer == 1:
    print(-1)
else:
    print(answer)
    