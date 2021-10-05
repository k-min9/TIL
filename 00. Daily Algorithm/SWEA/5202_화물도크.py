import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    # 신청서 수
    N = int(input())
    # 스케쥴 내용
    schedules = [list(map(int, input().split())) for _ in range(N)]
    schedules.sort(key=lambda x: (x[1], x[0]))

    answer = 0
    last = 0
    for s, e in schedules:
        if s >= last:
            answer += 1
            last = e

    print(f'#{tc+1}', answer)
