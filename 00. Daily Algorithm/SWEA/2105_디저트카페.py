import sys
sys.stdin = open('input.txt')

# 상수
MOVES = ((1, 1), (1, -1), (-1, -1), (-1, 1))


def dfs(now, dir):
    global answer
    x, y = now

    if now == start and len(desserts) >= 4:  # 시작점에 도달한 경우 (되돌아오는 경우 제외)
        answer = max(answer, len(desserts))
        return

    for idx, d in enumerate(MOVES):
        # 사각형의 조건 : 거쳐온 이동 방향을 다시 이용할 수 없음
        if idx not in directions:
            nx, ny = x + d[0], y + d[1]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maps[nx][ny] not in desserts:
                visited[nx][ny] = 1
                desserts.add(maps[nx][ny])

                if idx != dir:  # 이전과 이동방향이 바뀌는 경우
                    directions.append(dir)
                    dfs((nx, ny), idx)
                    directions.pop()

                else:  # 이전과 이동방향이 같은 경우
                    dfs((nx, ny), dir)

                visited[nx][ny] = 0
                desserts.remove(maps[nx][ny])


for tc in range(int(input())):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]

    answer = -1

    for i in range(N):
        for j in range(N):
            visited = [[0]*N for _ in range(N)]

            directions = list()  # 이동 방향 저장
            desserts = set()  # 디저트 종류 저장

            start = (i, j)
            dfs(start, 0)

    print(f'#{tc+1}', answer)
