import sys
sys.stdin = open('input.txt')


def calc(node):
    if node_value[node] != 0:
        return node_value[node]
    else:
        if node_oper[node] == '+':
            return calc(node_left[node]) + calc(node_right[node])
        elif node_oper[node] == '-':
            return calc(node_left[node]) - calc(node_right[node])
        elif node_oper[node] == '*':
            return calc(node_left[node]) * calc(node_right[node])
        elif node_oper[node] == '/':
            return calc(node_left[node]) / calc(node_right[node])


for t in range(10):
    N = int(input())

    node_value = [0]*(N+1)
    node_oper = [0]*(N+1)
    node_left = [0]*(N+1)
    node_right = [0]*(N+1)

    for _ in range(N):
        tmp = list(input().split())
        if len(tmp) == 2:
            node_value[int(tmp[0])] = int(tmp[1])
        else:
            node_oper[int(tmp[0])] = tmp[1]
            node_left[int(tmp[0])] = int(tmp[2])
            node_right[int(tmp[0])] = int(tmp[3])

    print(f'#{t+1}', int(calc(1)))
