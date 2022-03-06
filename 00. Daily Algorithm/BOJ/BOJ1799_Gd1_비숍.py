'''
백트래킹으로 보임
N-Queen이 Gold5인데 얘는 Gold1...?
아마 한 Row에 하나만 두는게 없어져서 더 어려워지나본데...
10초 = 2억번 계산 가능
'''
import sys
input = sys.stdin.readline


# 상수
MOVES = [(-1, -1), (-1, 1), (1, 1), (1, -1)]


N = int(input())
graphs = list()
position = list()
visited_max = 0
for i in range(N):
    next = list(map(int, input().split()))
    graphs.append(next)
    for j in range(N):
        if next[j] == 1:
            position.append((j, i))
            visited_max += 1

def dfs(x, y, cnt, visited):
    if len(visited) == visited_max:
        global answer
        answer = max(answer, cnt)
        return
    
    # (x, y)에 비숍 두면 메워지는 visited 체크
    visited_tmp = set()
    visited_tmp.add((x, y))
    for dx, dy in MOVES:
        nx = x
        ny = y
        while True:
            nx = nx + dx
            ny = ny + dy
            if 0<=nx<N and 0<=ny<N:
                if graphs[ny][nx] == 1:
                    visited_tmp.add((nx, ny))
            else:
                break
    visited_tmp = visited_tmp - visited

    # 다음 dfs
    visited = visited | visited_tmp
    if len(visited) == visited_max:
        answer = max(answer, cnt + 1)
        return
    for x, y in position:
        if (x, y) not in visited:
            dfs(x, y, cnt + 1, visited)
    visited = visited - visited_tmp

answer = 0
for x, y in position:
    dfs(x, y, 0, set())

print(answer)

'''
1차 시도 실패 : 시간 초과
아무리 10초여도 시간초과 되는구만 이거~
>> 평소 체스 문제 처럼 흰색과 검은색을 나눠서 분할 정복하면 시간을 1/4로 줄일 수 있을 것 같기는한데...
그 외에도 대각선을 축으로 하는 마름모로 봐서 row를 만드는 방식등을 사용하긴 했는데... 밑에 방식이 다 뒤집었다.
'''
'''
찾아보니 그 위가 있다. 이분매칭. 플래티넘급 문제 개념이다.
참고 : https://blog.naver.com/kks227/220807541506
남들 덧셈 뺄셈할때 곱셈 나눗셈하는 이 느낌... 이게 알고리즘이구만 싶긴하다.
속도는 N=10 기준 거의 50~100배 차이난다. 더 커지면 더 벌어질테고
'''

# n = int(input())
# table = [list(map(int, input().split())) for _ in range(n)]
# right = [[0] * n for _ in range(n)]
# left = [[0] * n for _ in range(n)]
# r, l = 1, 1

# for j in range(n):
#     i = 0
#     while i<n and 0<=j:
#         if table[i][j] == 1:
#             right[i][j] = r
#         i += 1; j -= 1
#     r += 1
# for i in range(1, n):
#     j = n-1
#     while i<n and 0<=j:
#         if table[i][j] == 1:
#             right[i][j] = r
#         i += 1; j -= 1
#     r += 1

# for j in range(n-1, -1, -1):
#     i = 0
#     while i<n and j<n:
#         if table[i][j] == 1:
#             left[i][j] = l
#         i += 1; j += 1
#     l += 1
# for i in range(1, n):
#     j = 0
#     while i<n and j<n:
#         if table[i][j] == 1:
#             left[i][j] = l
#         i += 1; j += 1
#     l += 1

# # 1<= l, r <=2*n
# link = [[] for _ in range(l)]
# for i in range(n):
#     for j in range(n):
#         if table[i][j]:
#             link[left[i][j]].append(right[i][j])

# def dfs(idx):
#     visited[idx] = True
#     l = link[idx]
#     for p in l:
#         if r2l[p] == 0 or (not visited[r2l[p]] and dfs(r2l[p])):
#             r2l[p] = idx
#             l2r[idx] = p
#             return True
#     return False

# l2r = [0] * (2*n)
# r2l = [0] * (2*n)
# ans = 0
# for i in range(1, 2*n):
#     visited = [False] * (2*n)
#     if dfs(i):
#         ans += 1
# print(ans)
