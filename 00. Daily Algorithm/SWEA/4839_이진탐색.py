import sys
sys.stdin = open('input.txt')


def my_bisect(target, lo=1, hi=None):
    speed = 0
    while lo < hi:
        mid = (lo+hi)//2
        speed += 1
        if mid == target:
            return speed
        elif mid < target:
            lo = mid
        else:
            hi = mid
    return speed


T = int(input())

for tc in range(T):

    hi, Pa, Pb = map(int,input().split())
    lo = 1

    speed_a = my_bisect(Pa, 1, hi)
    speed_b = my_bisect(Pb, 1, hi)

    if speed_a < speed_b:
        answer = 'A'
    elif speed_a == speed_b:
        answer = '0'
    else:
        answer = 'B'

    print(f'#{tc + 1}', answer)
