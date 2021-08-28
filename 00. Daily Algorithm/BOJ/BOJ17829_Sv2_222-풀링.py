'''
크기 1이 될때까지 재귀
'''
import sys
input = sys.stdin.readline

def calc(matrix):
    # 1*1 이면 리턴
    if len(matrix) == 1:
        return matrix[0][0]

    m = len(matrix)
    k = m//2

    # 리턴 행렬
    result = [[0]*k for _ in range(k)]

    for i in range(0,m,2):
        for j in range(0,m,2):
            # 2번째로 큰 수 구하기
            temp = sorted([matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]])
            temp = temp[-2]
            result[i//2][j//2] = temp

    # 재귀이용
    return calc(result)

# 입력
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

print(calc(matrix))