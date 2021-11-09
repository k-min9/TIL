'''
numpy : 다차원 행렬 처리를 하는데 필요한 여러 기능을 제공 (설치 : pip install numpy)
다차원배열(ndarray) - rank: 배열의 차원, shape: 차원의 크기를 튜플로 표시
'''
import numpy as np
# print(dir(np))

# 반환 받아야 되는 방식의 연산
a = [1, 4, 9]
a = np.sqrt(a)
# print(a)

# arange : 연속되거나 일정한 규칙을 가진 숫자, 데이터 형태 지정
v1=np.arange(5)
v2=np.arange(1,10,2, dtype=int)
v3=np.arange(3.5,10.5,2, dtype=float)
v4=np.arange(1,10,2)**2 # 제곱값 생성
# print(v1)
# print(v2)
# print(v3)
# print(v4)

# reshape : 행렬 만들기
v1=np.arange(12)
v2=v1.reshape(2,6)  # order 기본값 : 'C' 생략, 사이즈 딱 맞아야 함 2 * 6 = 12
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]]
v3=v1.reshape(2,6, order='F')
# [[ 0  2  4  6  8 10]
#  [ 1  3  5  7  9 11]]
# print(v1) # [ 0  1  2  3  4  5  6  7  8  9 10 11]
# print(v2)
# print(v3)

# 행렬 연산 (add, subtract, mulitply:1대1 합, 차, 곱, dot: 행렬 곱)
arr = np.arange(1,5).reshape(2,2)
v1 = np.multiply(arr, arr)
v2 = np.dot(arr, arr)
# print(v1)
# print(v2)

# 다차원 & 기타 보조
v1 = np.arange(12).reshape(2,3,2)
# print(np.amax(v1))
# print(np.amin(v1))
# print(dir(v1))
# print(v1.dtype)
# print(v1.shape)