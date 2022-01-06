'''
게이트 일일히 검사시 시간 초과가 나오는 견적이다.
도킹 결과 게이트와 이전 게이트를 union하는 방식으로 확 줄일 수 있다. => 분리집합(union-find)
'''
import sys
input = sys.stdin.readline


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)
    parents[b] = a  # sorted


G = int(input())
P = int(input())
parents = list(range(G+1))

g_list = [int(input()) for _ in range(P)]

answer = 0
for g in g_list:
    gate = find(g)  # 도킹 시도 게이트
    if gate == 0:
        break
    answer += 1
    union(gate-1, gate)  # 도킹 성공시 전 게이트와 유니온 (순서 주의)

print(answer)
    

