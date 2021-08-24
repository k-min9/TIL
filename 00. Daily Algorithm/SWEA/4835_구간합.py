import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    cases = list(map(int, input().split()))

    memos = []
    for i in range(N-M+1):
        memo = 0
        for j in range(M):
            memo += cases[i+j]
        memos.append(memo)

    print(f'#{t}', max(memos)-min(memos))
