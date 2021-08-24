import sys
from itertools import combinations
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):

    N, K = map(int, input().split())

    answer = 0
    for i in combinations(range(1, 13), N):
        if sum(i) == K:
            answer = answer + 1

    print(f'#{tc + 1}', answer)
