import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    buses = [0]*5001
    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            buses[i] += 1

    P = int(input())
    answer = list()
    for _ in range(P):
        answer.append(buses[int(input())])

    print(f'#{t+1}', *answer)
