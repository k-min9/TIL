'''
visited?
'''

import sys
input = sys.stdin.readline


N, Q = map(int, input().split())

visited = set()
for _ in range(Q):
    path = []
    node = int(input())
    n = node

    # path 적기
    while n:
        path.append(n)
        n = n // 2
    
    # print(node, ':' , path, visited)

    # 네
    answer = 0
    for p in path:
        if p in visited:
            answer = p  # 갱신
    
    # 땅 점유
    if answer==0:
        visited.add(node)

    print(answer)