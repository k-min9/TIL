import sys
sys.stdin = open('input.txt')


def chk(i):
    x = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
    return max(buildings[i]-x, 0)


for t in range(1, 11):

    N = int(input())
    buildings = list(map(int,input().split()))

    answer = 0
    for i in range(2, N-2):
        answer = answer + chk(i)
    print(f'#{t}', answer)
