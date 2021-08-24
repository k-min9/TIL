import sys
sys.stdin = open('input.txt')


def count_k(arr):
    count = arr[0]
    count_list = list()
    last_num = arr[0]
    for num in arr[1:]:
        if num == 1:
            if last_num == 0:
                last_num = 1
                count = 1
            else:
                count = count + 1
        else:
            if last_num == 1:
                last_num == 0
                count_list.append(count)
                count = 0
    if count != 0:
        count_list.append(count)

    # 반환용 재활용
    count = 0
    for c in count_list:
        if c == K:
            count += 1
    return count


T = int(input())

for tc in range(T):

    puzzles = list()
    N, K = map(int, input().split())
    for i in range(N):
        puzzles.append(list(map(int, input().split())))

    answer = 0
    for i in range(N):
        answer += count_k(puzzles[i])

    puzzles = list(zip(*puzzles))
    for i in range(N):
        answer += count_k(puzzles[i])

    print(f'#{tc + 1}', answer)
