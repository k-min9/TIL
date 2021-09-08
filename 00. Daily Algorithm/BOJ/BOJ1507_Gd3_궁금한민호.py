'''
접근 : 역 플로이드 와샬???????
어딘가를 지나가서 온 간선이 현재 간선과 같다 = 삭제
'''
import sys
input = sys.stdin.readline

# 상수
INF = 1e9

N = int(input())
graphs = [list(map(int, input().split())) for _ in range(N)]

# 지울 간선
answer = 0
erase = []
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != k and k != j and i != j:
                if graphs[i][k] + graphs[k][j] == graphs[i][j]:
                    erase.append((i, j))
                # 이 결과물을 다시 플로이드 와셜해서 같은 그래프가 안나오면 -1
                elif graphs[i][k] + graphs[k][j] < graphs[i][j]:
                    answer = -1

# for g in graphs:
#     print(*g)
# print('===========')

if answer != -1:
    for i, j in erase:
        graphs[i][j] = 0

    # 2차원 배열을 1차원 배열로(파이써닉)
    graphs = [j for i in graphs for j in i]
    answer = sum(graphs)//2

print(answer)