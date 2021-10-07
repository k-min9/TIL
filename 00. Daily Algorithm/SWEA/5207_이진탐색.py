import sys
sys.stdin = open('input.txt')


# x를 찾아라, 탐색 과정에서 양쪽구간을 번갈아 선택(...?)
def binary_search(x):
    l, r = 0, N-1

    # 양쪽구간을 번갈아 선택
    flag = -1
    while l<=r:
        mid = (l+r)//2
        if list_A[mid] < x:
            l = mid + 1

            if flag == 0:
                return False
            flag = 0

        elif list_A[mid] > x:
            r = mid - 1

            if flag == 1:
                return False
            flag = 1

        else:
            return True
    return False

for tc in range(int(input())):
    # 리스트A(테스트 대상), 리스트B(얘가 들어있나.)
    N, M = map(int, input().split())
    list_A = list(map(int, input().split()))
    list_A.sort()
    list_B = list(map(int, input().split()))

    answer = 0
    for b in list_B:
        if binary_search(b):
            answer += 1

    print(f'#{tc+1}', answer)
