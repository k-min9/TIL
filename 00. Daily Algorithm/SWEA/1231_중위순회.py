import sys
sys.stdin = open('input.txt')


# LUR
def calc(node):
    if node > N:
        return ''
    if node <= N:
        return calc(2*node) + nodes[node] + calc(2*node+1)


for t in range(10):
    N = int(input())

    nodes = [0]*(N+1)
    for i in range(1, N+1):
        tmp = input().split()
        nodes[i] = tmp[1]

    print(f'#{t+1}', calc(1))
