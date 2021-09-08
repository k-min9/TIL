'''
접근 : 이렇게 대놓고 개념이 제목에 적혀있으면 안풀고 갈 수가 없지
크루스칼 - 프림 개념 정리는 1197번 참조
'''

import sys
input = sys.stdin.readline

# 지원함수 1 : 유니온 - 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if b < a:
        parent[a] = b
    else:
        parent[b] = a

# 지원함수 2 : find - 루트 노드를 찾을때까지 재귀적으로 반환
def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

# 정점 수, 간선 수, 턴의 수
N, M, K = map(int, input().split())

# 간선 정보 정리
graphs = []
for w in range(1, M+1):
    a, b = map(int, input().split())
    # 자동 순서 정리 꿀!
    graphs.append((w, a, b))

answers = [0]*K
for turn in range(K):
    answer = 0
    cnt = 0
    # 서로소 집합 자료구조용 입력 정보
    parent = list(range(N+1))
    for weight, start, end in graphs[turn:]:
        # 루트가 같음 = 사이클 = 잇지 않는다.
        if find(start) != find(end):
            union(start, end)
            answer += weight
            cnt += 1
        if cnt == N-1:
            answers[turn] = answer
            break
    else:
        break

print(*answers)

'''
마지막에 else break 추가해봤는데 딱히 속도 변화는 없었다. 흐음
'''