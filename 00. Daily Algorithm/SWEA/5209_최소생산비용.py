import sys
sys.stdin = open('input.txt')


def backtrack(visit, cost, now):
    global answer

    if cost >= answer:
        return

    if visit == (1<<N)-1:
        answer = cost
        return

    for next in range(N):  # 직원 체크
        if not visit & (1<<next):
            backtrack(visit|(1<<next), cost+costs[now][next], now+1)


for tc in range(int(input())):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    answer = 1500

    backtrack(0, 0, 0)

    print(f'#{tc+1}', answer)
