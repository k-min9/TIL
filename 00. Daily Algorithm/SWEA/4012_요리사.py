import sys
sys.stdin = open('input.txt')


def cook():
    global answer
    tmp = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if visited[i] and visited[j]:
                tmp += recipes[i][j] + recipes[j][i]
            elif not visited[i] and not visited[j]:
                tmp -= recipes[i][j] + recipes[j][i]
    answer = min(answer, abs(tmp))


def dfs(start, cnt):
    if cnt == n // 2:
        cook()
        return

    for i in range(start, n):
        if not visited[i]:
            visited[i] = 1
            dfs(i + 1, cnt + 1)
            visited[i] = 0


for tc in range(int(input())):
    n = int(input())
    recipes = [list(map(int, input().split())) for _ in range(n)]
    answer = 987654321
    visited = [0]*n
    dfs(0, 0)

    print(f'#{tc+1}', answer)
