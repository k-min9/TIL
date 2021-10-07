import sys
sys.stdin = open('input.txt')


def backtrack(visit, prob, now):
    global answer

    if prob <= answer:
        return

    if visit == (1<<N)-1:
        answer = prob
        return

    # now = bin(visit).count('1') 되는데 느려짐 오ㅋㅋ 재밌다.
    for next in range(N):  # 직원 체크
        if not visit & (1<<next):
            backtrack(visit|(1<<next), prob*probs[now][next], now+1)


for tc in range(int(input())):
    N = int(input())
    probs = [list(map(lambda x: int(x)/100.0, input().split())) for _ in range(N)]
    answer = 0

    backtrack(0, 1.0, 0)

    print(f'#{tc+1} {answer * 100 :.6f}')
