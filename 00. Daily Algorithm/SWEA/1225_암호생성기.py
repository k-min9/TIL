import sys
sys.stdin = open('input.txt')
from collections import deque

for t in range(10):

    trash = int(input())
    nums = list(map(int, input().split()))
    nums = deque(nums)

    idx = 0
    while True:
        num = nums.popleft()
        idx = idx % 5 + 1
        num = num - idx
        if num <= 0:
            nums.append(0)
            break
        else:
            nums.append(num)

    print(f'#{t+1}', *nums)
