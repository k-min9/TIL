'''
기업 코테에 나올 법한 문제라서 바로 pick
10^18 이기 때문에 솔직히 돌리면 당연히 타임아웃

모든 노드에 대해 왼쪽 구슬 수와 오른쪽 수가 같기 때문에
절반+나머지는 왼쪽 절반은 오른쪽으로 떨어지게 된다 -> 이 개념을 마지막까지 돌리면 됨
'''
import sys
input = sys.stdin.readline

# 입력
N = int(input())
tree = [[-1,-1]] + [list(map(int, input().split())) for _ in range(N)]

# K번째 구슬의 위치
K = int(input())
cur_node = 1
while K >= 0:
    # 왼쪽 1 , 오른쪽 0
    direction = K % 2 

    # 아래로 내려감
    if tree[cur_node][0] != -1 and tree[cur_node][1] != -1:
        if direction:
            cur_node = tree[cur_node][0]
        else:
            cur_node = tree[cur_node][1]
        # 제일 중요
        K = K//2 + direction

    else:
        if tree[cur_node][0] == -1 and tree[cur_node][1] == -1:
            break
        elif tree[cur_node][1] == -1:
            cur_node = tree[cur_node][0]
        else:
            cur_node = tree[cur_node][1]

print(cur_node)
