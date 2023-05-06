# 알고리즘

## 개요

[기본 템플릿](BOJ/@@Template.py)

[함수 활용](BOJ/@@functions.py)

- 내가 알고리즘을 기본적으로 python으로 푸는 이유
- C++가 또 하나의 선택지가 될 수 있는 이유

- python3 vs pypy

pypy는 기본적으로 메모리를 많이 쓰는 대신에 빠르다. (메모리 <-> 연산속도의 트레이드 오프)

다만 pypy는 재귀에 약하기 때문에, 재귀가 많을 경우 그냥 python3가 유리하다.

- 힌트
  - dir(객체) : 사용할 수 있는 메서드 등을 정리
    - dir('234')
  - help(패키지) : 패키지 관련 설명 및 옵션 제공
    - help([].sort)
    - help(collections)
    - help(collections.defaultdict)

## 정리

### Python

#### 계산, 문자열 전처리

```python
from math import gcd
if a^b: 둘이 같지 않으면
eval() : 안의 내용을 연산함(속도 주의)
''.join(내용물) : 합치기
[].sort(reverse=True)
words = words.replace('..','') : 문자열 바꾸기, (while '..' in words)와 조합해서 엄청 많이 씀
ord(문자) / chr(정수)
```

#### 자료형, 함수 및 라이브러리

```python
s[:] = ~ : 얕은 복사 하는 법
s[::-1] : 뒤집기, 문자열 유효
zip() : 대각선 뒤집기에 자주 쓰임
collections.deque : append, appendleft, pop, popleft
collections.defaultdict(<list>) : default값을 빈 list로 가져서 관리가 편한 dictionary
collections.Counter(list) : 아이템 갯수를 계산해 딕셔너리 리턴 -> .most_common(순위)와 조합
for idx, num in enumerate(list, 시작 idx번호): 리스트의 내용물을 순서와 함께 반복
for key, value in dic.items(): 딕셔너리, 카운터 반복
c = sorted(c.items(), key = lambda x: (-x[1], x[0])) : 딕셔너리, 카운터 소트 예시
from heapq import heappop, heappush, heapify : 우선순위 큐(최소 힙) / 최대힙 : heappush(heap, -x), -heappop
from itertools import permutations, combinations : 순열, 조합
from bisect import bisect_left : 이진 검색, 사용전 sort 주의
```

#### BFS

준비물 : collections.deque(queue) + 필요하면 visited; 리스트 내지 set(if i in visited)

예제 : 16933. 벽부수고이동하기3 (부수기찬스 포함 3차원 visited)

#### DFS

준비물 : visited

```python
def dfs(cnt, answer):
    global answer_max, answer_min

    # 도달
    if cnt == N+1:
        answer_max = max(answer_max, answer)
        answer_min = min(answer_min, answer)
        return

    for i in range(10):
        if not chk[i]: 
            if cnt==0 or eval(answer[-1] + exp[cnt-1] + str(i)):
                chk[i] = 1
                dfs(cnt+1, answer + str(i)) 
                chk[i] = 0
```

#### DP

예제 : 1149.RGB거리 (개인 취향)

#### 위상정렬

준비물 : indegree 리스트, deque

예제 : 1005

#### Backtrack

예제: 9663 N-Queen, 10597 순열장난

#### 이분 탐색

예시)

```python
while left <= right:
    mid = (left + right) // 2
    if 조건:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1
```

#### 누적합

#### 투 포인터

예제) 2230. 수고르기, 15565. 귀여운 라이온

#### 다익스트라

준비물 : heapq, 시작값 0 나머지 전부 INF인 graph

예제 : 1753.최단경로

예시)

```python
distance = [INF] * (n+1)
distance[nodeStart] = 0
q = [[0, nodeStart]]

while q:
    dist, cur = heappop(q)
    # 이미 처리 됨 = 다음 루프
    if distance[cur] < dist:
        continue
    for dist_next, next in graphs[cur]:
        cost = dist + dist_next
        if cost < distance[next]:
            distance[next] = cost
            heappush(q, [cost, next])
```

#### 플로이드

예시)

```python
dist = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    dist[i][i] = 0

for u,w,c in fares:
    dist[u][w] = c
    dist[w][u] = c

for m in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            val = dist[i][m] + dist[m][j]
            if val < dist[i][j]:
                dist[i][j] = val
```

#### 벨만포드

#### 프림

예제 : 1647_도시 분할계획

#### 유니온-파인드

예제 : 1197.최소스패닝트리

예시)

```python
def union(a, b):
    a = find(a)
    b = find(b)
    if b < a:
        parent[a] = b
    else:
        parent[b] = a

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]
        
parent = list(range(V+1))     

##### 여기까지하면 크루스칼
answer = 0
# 간선을 하나씩 확인
for weight, start, end in edges:
    # 루트가 같음 = 사이클 = 잇지 않는다.
    if find(start) != find(end):
        union(start, end)
        answer += weight

print(answer)
```

#### 트라이

개요 : 문자열 검색 특화, 삼성 역량 테스트 B형 수준

#### 비트마스크 완전탐색

#### 2-SAT
