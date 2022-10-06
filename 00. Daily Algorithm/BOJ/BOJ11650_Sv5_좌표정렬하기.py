import sys
input = sys.stdin.readline

N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
nums.sort(key=lambda x: (x[0], x[1]))

for i in nums:
    print(i[0], i[1])
