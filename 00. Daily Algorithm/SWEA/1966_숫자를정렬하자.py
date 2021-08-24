import sys
sys.stdin = open('input.txt')


# 버블소트에는 슬픈 전설이 있습니다.
def my_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


T = int(input())

for tc in range(T):

    N = int(input())
    numbers = list(map(int, input().split()))
    numbers = my_sort(numbers)

    print(f'#{tc + 1}', *numbers)
