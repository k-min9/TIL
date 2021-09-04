import sys
input = sys.stdin.readline

# 소수판별
def is_prime(a):
    if a == 1 or a == 0:
        return False
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    return True

# 입력
T = int(input())
for _ in range(T):
    nums = int(input())
    while True:
        if is_prime(nums):
            print(nums)
            break
        nums += 1