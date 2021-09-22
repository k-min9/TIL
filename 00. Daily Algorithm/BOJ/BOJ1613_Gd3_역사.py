'''
사건수 400
관계수 50000
쿼리수 50000
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graphs = [[0]*n for _ in range(n)]
for i in range(k):
    a, b = map(int, input().split())
    # 순서대로
    graphs[a-1][b-1] = -1
    graphs[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graphs[i][j] == 0:
                if graphs[i][k] == 1 and graphs[k][j] == 1:
                    graphs[i][j] = 1
                elif graphs[i][k] == -1 and graphs[k][j] == -1:
                    graphs[i][j] = -1

for _ in range(int(input())):
    q1, q2 = map(int, input().split())
    print(graphs[q1-1][q2-1])

'''
플로이드 개꿀문제...!
'''