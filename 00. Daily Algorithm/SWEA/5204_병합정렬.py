import sys
sys.stdin = open('input.txt')


def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr

    return merge(merge_sort(arr[:n//2]), merge_sort(arr[n//2:]))


def merge(left, right):
    global answer
    if left[-1] > right[-1]:
        answer += 1

    ret = list()
    idx_left, idx_right = 0, 0
    len_left, len_right = len(left), len(right)

    while idx_left < len_left and idx_right < len_right:
        if left[idx_left] <= right[idx_right]:
            ret.append(left[idx_left])
            idx_left += 1
        else:
            ret.append(right[idx_right])
            idx_right += 1

    if idx_left < len_left:
        ret += left[idx_left:]
    else:
        ret += right[idx_right:]

    return ret


for tc in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))

    answer = 0
    nums = merge_sort(nums)

    print(f'#{tc+1}', nums[N//2], answer)
