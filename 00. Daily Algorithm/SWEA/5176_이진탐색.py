import sys
sys.stdin = open('input.txt')


# LUR
def make_bst(node):
    global cnt
    if node <= N:
        make_bst(2*node)
        answers[node] = cnt
        cnt += 1
        make_bst(2*node + 1)


for t in range(int(input())):
    N = int(input())

    answers = [0]*(N+1)
    cnt = 1
    make_bst(1)

    print(f'#{t+1}', answers[1], answers[N//2])
