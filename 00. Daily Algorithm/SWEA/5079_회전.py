import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):

    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    print(f'#{t+1}', nums[M%N])
