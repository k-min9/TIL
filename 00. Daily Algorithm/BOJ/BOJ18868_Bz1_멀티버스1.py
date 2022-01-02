'''
풀이보다 문제가 더 이해하는데 오래걸리는데 이거 어케 안되나...
요지는 리스트 서열순이 같은지 체크하는 것이다.
'''
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
universe = [list(map(int, input().split())) for _ in range(M)]
answer = 0

for planet in range(M):
    for i in range(M):
        arr_sort = sorted(universe[i])
        idx = []
        for j in universe[i]:
            idx.append(arr_sort.index(j) + 1)
        universe[i] = idx

for i in range(M - 1):
    for j in range(i + 1, M):
        if universe[i] == universe[j]:
            answer += 1

print(answer)