import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    # 점원 수, 선반 높이
    N, B = map(int, input().split())
    # 점원 키
    H = list(map(int, input().split()))

    now = {0}
    next = set()
    for h in H:
        while now:
            n = now.pop()
            next.add(n+h)
            next.add(n)
        now, next = next, now

    answer = sum(H)
    for n in now:
        if n>=B:
            answer = min(answer, n-B)

    print(f'#{tc+1}', answer)
