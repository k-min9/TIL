'''
시간초과 되기 딱 좋은 문제
숫자 배치하고 , + * 경우의 수 전부 돌리면 될거같은데?
곱하는거 전후로 죄다 더하고 곱하기 위치에 맞게 곱하자!
'''
import sys
input = sys.stdin.readline
from itertools import combinations, permutations


# def dfs(cur, qCnt, arr):
#     global answer
#     if qCnt == 0:
#         answer = max(answer, cur*sum(arr))
#         return cur * sum(arr)
#     else:
#         idx_list = range(len(arr))
#         for pick_cnt in range(1, len(arr)-qCnt+1):
#             for comb in combinations(idx_list, pick_cnt):
#                 tmp_arr = arr[:]
#                 comb = list(reversed(comb))
#                 temp_sum = 0
#                 for idx in comb:
#                     temp_sum += tmp_arr.pop(idx)                
#                 dfs(cur*temp_sum,qCnt-1,tmp_arr)


# 정수 수
N = int(input())
nums = list(map(int, input().split()))
# 더하기, 곱하기 연산자 수
P, Q = map(int, input().split())

# answer = 0
# dfs(1, Q, nums)
# print(answer)


## 다른분 코드
answer = 0
for per_case in permutations(nums): # 모든 숫자케이스
    for com_case in combinations(range(N-1), Q): # 곱셈 위치 고르기
        multiply_location = [-1] #처음꺼 예외케이스로 -1 넣어주기
        multiply_location.extend(com_case)
        multiply_location.append(N)

        # 곱하는 부분 전 후로 죄다 더해버리면 된다.
        area_sum = []
        for idx in range(len(multiply_location) - 1):
            left, right = multiply_location[idx], multiply_location[idx + 1]
            area_sum.append(sum(per_case[left + 1 : right + 1]))

        val = 1
        for item in area_sum: val*=item
        answer = max(answer, val)
print(answer)

'''
올만에 어려운 문제 ㄷㄷㄷ
'''