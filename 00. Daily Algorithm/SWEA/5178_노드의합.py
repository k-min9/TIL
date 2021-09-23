import sys
sys.stdin = open('input.txt')

for t in range(int(input())):
    # 총 노드수, 리프 노드의 개수, 쿼리
    N, M, L = map(int, input().split())

    # 리프 노드가 아닌 모든 노드가 자식을 최소 둘 가지게 0 노드 추가
    node_value = [0] * (N+2)
    for _ in range(M):
        node, value = map(int, input().split())
        node_value[node] = value

    # 좀 만 생각해봐도 역순으로 더해 올라와야 하더라;;
    for i in range(N-M, 0, -1):
        node_value[i] = node_value[2*i] + node_value[2*i+1]

    print(f'#{t+1}', node_value[L])
