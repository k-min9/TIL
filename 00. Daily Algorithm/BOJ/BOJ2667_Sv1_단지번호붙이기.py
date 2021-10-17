'''
2차원 유니온-파인드
'''

import sys
input = sys.stdin.readline
from collections import defaultdict


def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        a, b = b, a
    parents[b] = a


N = int(input())
maps = [list(map(int, list(input().rstrip()))) for _ in range(N)]
MOVES = ((0, 1), (1, 0), (-1, 0), (0, -1))
parents = {(i, j): (i, j) for i in range(N) for j in range(N)}
for x in range(N):
    for y in range(N):
        if maps[x][y]:
            for dx, dy in MOVES:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and maps[nx][ny]:
                    if find((x, y)) != find((nx, ny)):
                        union((x, y), (nx, ny))

answer = defaultdict(int)
for parent in parents:
    x, y = parent
    if maps[x][y]:
        answer[find(parent)] += 1

answer_arr = []
for num in answer:
    answer_arr.append(answer[num])
answer_arr.sort()

print(len(answer_arr))
for num in answer_arr:
    print(num)