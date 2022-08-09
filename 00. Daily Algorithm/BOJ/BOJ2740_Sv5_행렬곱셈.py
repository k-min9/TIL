'''
~분할정복 Festival~ 6/10
분할 정복 없이 풀리는디?
'''
import sys
input = sys.stdin.readline 

# 입력
N, M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
M, K = map(int,input().split())
B = [list(map(int,input().split())) for i in range(M)]
  
# 계산
for i in range(N):
    for j in range(K):
        tmp = 0
        for l in range(M):
            tmp += A[i][l]*B[l][j]
        print(tmp, end=' ')
    print()

'''
행렬을 사분할 하는 슈트라센 알고리즘을 사용하면 더 빨라진다고 한다
O(ㅜ^3) -> O(N^2.807)
'''