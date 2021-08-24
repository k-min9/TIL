import sys
sys.stdin = open('input.txt')


# 대각선 신경 안써도 되는 N-queen
def my_queen(depth):
    global ret, ans

    # 백트래킹 요소 : 총합이 미쳐 날 뜀
    if ans < ret:
        return

    # 도착(위에서 이미 크기 비교 해서 min 안써도 됨)
    if depth == N:
        ans = ret
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            ret += graphs[depth][i]
            my_queen(depth+1)
            visited[i] = 0
            ret -= graphs[depth][i]


T = int(input())
for t in range(T):
    N = int(input())
    graphs = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ret, ans = 0, 501
    my_queen(0)

    print(f'#{t+1}', ans)
