import sys
sys.stdin = open('input.txt')


for t in range(10):
    N = int(input())
    graphs = [list(map(int, input().split())) for _ in range(N)]
    graphs = list(zip(*graphs))

    answer = 0
    for graph in graphs:
        #왼쪽이 N 오른쪽이 S
        flag = False
        for g in graph:
            if g == 1:
                flag = True
            elif g == 2 and flag:
                answer += 1
                flag = False

    print(f'#{t+1}', answer)
