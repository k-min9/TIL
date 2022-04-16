'''
입력값이 대놓고 1,000,000,000,000,000,000 이러면 분할정복을 쓰라는게 보여서 오히려 견적 낼 필요 없이 써야할 알고리즘이 좁혀진다.
문제는 어떻게 곱셈의 형태로 만들어서 나누냐는 건데...
행렬 곱셈 즉 선형대수학으로 해결할 수 있다고 생각한다.
'''
import sys
input = sys.stdin.readline

# 상수
MOD = 1000000007


# 행렬 곱
def matrix_mul(mat1, mat2):
    ret = list()
    for i in range(2):
        ret.append(list())
        for j in range(2):
            temp = 0
            for k in range(2):
                temp += mat1[i][k] * mat2[k][j]
            ret[i].append(temp%MOD)
    return ret

# 행렬 거듭제곱
def matrix_power(mat, p):
    if p == 1:
        return mat
    else:
        mat_divide = matrix_power(mat, p // 2)
        if p % 2 == 0:
            return matrix_mul(mat_divide, mat_divide)
        else:
            return matrix_mul(matrix_mul(mat_divide, mat_divide), mat)

N = int(input())
mat = [[1, 1], [1, 0]]
print(matrix_power(mat, N)[0][1])

