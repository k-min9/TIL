import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):

    cases = input().rstrip()
    # 최종 막대기 수, 레이저가 벌어올 포인트, 발사 가능 상태 여부, 최초의 막대 수
    answer = 0
    points = 0
    shot = 0
    new = 0
    
    for case in cases:
        if case == '(':
            shot = 1
            points = points + 1
            new = new + 1
        else:
            points = points - 1
            if shot == 1:
                shot = 0
                new = new - 1
                answer = answer + points

    print(f'#{t + 1}', answer + new)
