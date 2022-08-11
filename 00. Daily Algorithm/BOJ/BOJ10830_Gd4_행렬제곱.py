'''
~분할정복 Festival~ 7/10
곱셈 분할 정복의 행렬 버전?
'''
import sys
input = sys.stdin.readline

# 상수
MOD = 1000

# 행렬 곱
def multi(mat1, mat2, size):
  mat3 = [[0]*size for _ in range(size)]
  for i in range(size): 
    for j in range(size): 
      for l in range(size): 
        mat3[i][j] += mat1[i][l]*mat2[l][j] % MOD
      mat3[i][j] %= MOD
  return mat3

# 분할 정복
def square(mat, N):
  size = len(mat)
  if N == 1: 
    return mat
  elif N%2 == 0: 
    square_mat = square(mat, N//2)
    return multi(square_mat, square_mat, size)
  else: 
    square_mat = square(mat, N//2)
    return multi(mat, multi(square_mat,square_mat,size), size)


# 입력
N, B = map(int, input().split()) # A의 B제곱
A = [list(map(int, input().split())) for _ in range(N)]

C = [[0]*N for _ in range(N)]


C = square(A,B)
for c in C:
  for answer in c:
    print(answer%MOD, end=' ')
  print()
