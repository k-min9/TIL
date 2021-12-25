'''
탈출은 무조건 바깥에서 일어나니 바깥에서 역으로 들어가는 방법
탈출에 성공하면 그 동안 지나간 곳은 모두 탈출 가능하다고 적는 방법

견적은 어느쪽도 넉넉!
이렇게 싱글벙글 어느쪽으로 풀 지 고민되는 문제는 오랜만이다.
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000000)


def dfs(x, y):
    if x<0 or x>=M or y<0 or y>=N:
        return True

    # 이미 탈출 성공 루트
    if visited[y][x] == 3:
        return True
    # DFS 중 지나간 장소
    if visited[y][x] == 1:
        return False       
    # 이미 탈출 실패 루트
    if visited[y][x] == 2:
        return False
    else:
        visited[y][x] = 1
        dx, dy = directions[maps[y][x]]
        nx = x + dx
        ny = y + dy

        result = dfs(nx, ny)
        if result:
            visited[y][x] = 3
        else:
            visited[y][x] = 2
        return result

N, M = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
directions = {'U': (0, -1), 'R': (1, 0), 'D': (0, 1), 'L': (-1, 0)}

answer = 0
for y in range(N):
    for x in range(M):
        if dfs(x, y):
            answer += 1

print(answer)



'''
크 진짜 이상하게 잘 풀었다!
'''