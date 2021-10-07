import sys
sys.stdin = open('input.txt')


def quick_sort(left, right):
    if left >= right:
        return

    # pivot : 제일 왼쪽
    start, end = left+1, right-1
    pivot = left  # 굳이 언급

    while start <= end:
        while start <= end and nums[start] <= nums[pivot]:
            start += 1
        while start <= end and nums[end] >= nums[pivot]:
            end -= 1
        if start <= end:
            nums[start], nums[end] = nums[end], nums[start]

    nums[pivot], nums[end] = nums[end], nums[pivot]

    quick_sort(left, end)
    quick_sort(end+1, right)


for tc in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))

    quick_sort(0, N)

    print(f'#{tc+1}', nums[N//2])
