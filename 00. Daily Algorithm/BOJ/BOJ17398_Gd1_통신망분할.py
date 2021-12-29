'''
Union-find 문제
접근 : 역으로 조합하면서 발생하는 비용을 계산하면 된다.
'''
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])
 
def union(x,y):
    X = find(x)
    Y = find(y)

    # 이 문제 전용 풀이(계산 필요)
    if X == Y:
        return 0 
    else:
        if weights[X] < weights[Y]:
            X, Y = Y, X

        size_a, size_b = weights[X], weights[Y]
        weights[X] += weights[Y]
        parent[Y] = X
        return size_a*size_b
            
        
# 입력 (노드 수, 연결 수, 쿼리 수)
N, M, Q = map(int,input().split())
  
parent = list(range(N+1))
weights = [1]*(N+1)
connections = [[],]
check = [True]*(M+1)
for _ in range(M):
    x, y = map(int, input().split())
    connections.append((x,y))

queries = []
 
for _ in range(Q):
    x = int(input())
    queries.append(x)
    check[x] = False
 
 
for i in range(1,M+1):
    if check[i]:
        x,y = connections[i]
        union(x, y)

answer = 0
while queries:
    query = queries.pop()
    x, y = connections[query]
    answer += union(x, y)

print(answer)