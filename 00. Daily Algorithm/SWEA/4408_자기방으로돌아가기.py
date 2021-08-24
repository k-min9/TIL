import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    rooms = [0]*201
    for _ in range(N):
        a, b = map(int, input().split())
        a, b = (a+1)//2, (b+1)//2
        if a > b:
            a, b = b, a
        for i in range(a, b+1):
            rooms[i] += 1

    print(f'#{t+1}', max(rooms))

