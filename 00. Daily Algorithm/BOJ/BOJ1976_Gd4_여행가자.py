'''
접근 : Union-Find해서 같은 parent를 갖나 확인하면 되지 않을까? 싶어서 복습 차원
'''
import sys
input = sys.stdin.readline


def union(a, b):
    a = find(a)
    b = find(b)

    if b<a:
        parent[a] = b
    else:
        parent[b] = a


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


# 도시의 수, 여행 계획
N = int(input())
M = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
travels = list(map(int, input().split()))

# 묶고
parent = list(range(N+1))
for y in range(N):
    for x in range(N):
        if maps[y][x] == 1:
            union(x+1, y+1)

# 결과 발표
answer = set()
for travel in travels:
    answer.add(parent[travel])

if len(answer) == 1:
    print('YES')
else:
    print('NO')