import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    answer = [0, 0, 0, 0, 0]

    while not N % 2:
        answer[0] = answer[0] + 1
        N = N // 2
    while not N % 3:
        answer[1] = answer[1] + 1
        N = N // 3
    while not N % 5:
        answer[2] = answer[2] + 1
        N = N // 5
    while not N % 7:
        answer[3] = answer[3] + 1
        N = N // 7
    while not N % 11:
        answer[4] = answer[4] + 1
        N = N // 11

    print(f'#{t}', *answer)
