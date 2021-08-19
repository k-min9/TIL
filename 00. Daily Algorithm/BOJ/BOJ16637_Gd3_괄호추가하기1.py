'''
from 16639 괄호 추가하기3 의 중첩된 괄호 없는 버전
괄호 계산 모든 가능성 다 하고, 그 이후 왼쪽에서 계산한다.
'''
import sys
import operator
input = sys.stdin.readline

def dfs(depth, result):
    # 종료 조건 (ops회 연산)
    if depth >= N//2:
        global ans
        ans = max(ans, result)
        return

    # 괄호로 묶지 않는다. = 이전 + 다음    
    dfs(depth+1, ops[depth](result, nums[depth+1]))

    # 괄호로 묶는다 = 이전 + 괄호 계산
    if depth + 1 < N//2:
        # 괄호 부분
        tmp = ops[depth+1](nums[depth+1], nums[depth+2])
        # 이전 계산
        dfs(depth+2, ops[depth](result, tmp))
    return


N = int(input())
expressions = input().rstrip()
nums = list(map(int, expressions[::2]))
ops = list(map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, expressions[1::2]))

ans = -2**31
dfs(0, nums[0])
print(ans)

'''
get으로 operator 빌트인 함수를 담았다. 이게 되는게 신기하네.
'''