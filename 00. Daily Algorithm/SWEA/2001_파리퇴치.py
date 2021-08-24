import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):

    N, M = map(int, input().split())
    flies = graph = [[0]*(N+1) for _ in range(N+1)]

    for i in range(N):
        flies[i+1] = [0] + list(map(int, input().split()))

    # for i in range(N+1):
    #     print(*flies[i])

    # 누적 합
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            flies[i][j] = flies[i - 1][j] + flies[i][j - 1] + flies[i][j] - flies[i - 1][j - 1]

    # for i in range(N+1):
    #     print(*flies[i])

    answer = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            answer = max(answer, flies[i + M][j + M] - flies[i][j + M] - flies[i + M][j] + flies[i][j])

    print(f'#{tc + 1}', answer)
