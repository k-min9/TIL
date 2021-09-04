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

# 입력
nums = int(input())

while True:
    # 펠린드롬
    chk = str(nums)
    if chk == chk[::-1]:
        if is_prime(nums):
            print(nums)
            break
    nums += 1