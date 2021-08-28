import sys
input = sys.stdin.readline

# 서로소 집합 자료구조 (합치기 찾기 자료구조)

# 지원함수 1 : 유니온 - 합치기
def union(a, b):
    a = find(a)
    b = find(b)

    # 갱신 내지 재정의
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

# 정점 수, 관계 수
N, M = map(int, input().split())

# 서로소 집합용 입력 정보
parent = list(range(N+1))

# 간선 정보 정리
for _ in range(M):
    a, b= map(int, input().split())
    union(a,b)


# 그루핑
groups = [set() for _ in range(N+1)]
for i in range(1, N+1):
    groups[find(i)].add(i)

#print(groups)
# CTP 왕국, 한솔 왕국, 동맹 기회
C, H, K = map(int, input().split())

# 출력
answer = 0
answers = list()
for group in groups:
    if C in group:
        answer += len(group)
    elif not H in group:
        answers.append(len(group))
answers.sort(reverse=True)

print(answer + sum(answers[:K]))