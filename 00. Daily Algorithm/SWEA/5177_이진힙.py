import sys
sys.stdin = open('input.txt')
from heapq import heapify

for t in range(int(input())):
    N = int(input())
    nodes = list(map(int, input().split()))

    graphs = list()
    for node in nodes:
        graphs.append(node)
        heapify(graphs)

    answer = 0
    while N:
        N = N//2
        if N:
            answer += graphs[N-1]

    print(f'#{t+1}', answer)
