'''
사이클에 속하지 않는 노드 구하라는거 어렵게도 썼다.
다들 방향성 있는 노드니까 DFS로 할 거 알고 있다.
위상정렬이나 서로소집합도 가능할 것 같은데 흠...
'''

import sys
input = sys.stdin.readline

# 테스트 케이스
T = int(input())

for _ in range(T):
    n = int(input())  # 학생 수
    graphs = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)  # 현재 방문 중인 곳 포함

    ans = 0

    for i in range(1, n+1):

        if visited[i]:
            continue  # 다음으로
    
        cycle = []  # 일단 지나간 루트를 쭉 적는다.
        visited[i] = 1  # 예시 : 1번 학생부터 시작
        cycle.append(i)
        next = graphs[i]  # 예시 : 3번 학생 지목
        if i == next:
            ans = ans + 1
            continue
        while(not visited[next]):
            visited[next] = 1  # 방문
            cycle.append(next)
            next = graphs[next]
            if visited[next]:
                for j in range(len(cycle)):
                    if cycle[j] == next:  # 여기서부터 사이클
                        ans = ans + len(cycle) - j
                    # print('c', cycle, ans)
    print(n-ans)

'''
그ㅡ런 생각은 DFS가 자유자재로 나오게 되고 생각하자
'''

