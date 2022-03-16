'''
대놓고 분리 집합 / 유니온-파인드 문제
'''
import sys
input = sys.stdin.readline


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(x, y):
    x, y = find(x), find(y)

    # 이번 문제는 무조건 X가 parent가 되서 고민 여지가 없음
    if x != y:
        parent[y] = x
        number[x] += number[y]
    print(number[x])

for _ in range(int(input())):
    num = int(input())
    parent, number = {}, {}
    for i in range(num):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        union(a, b)