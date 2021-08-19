'''
from 16639 괄호 추가하기3 의 중첩된 괄호 없는 버전
괄호 계산 모든 가능성 다 하고, 그 이후 연산 순서대로 계산한다 >> 연산을 컴퓨터에 맡길수있다.(eval)
'''
import sys
input = sys.stdin.readline

def dfs(depth, result):
    # 종료 조건 (ops회 연산)
    if depth >= N//2:
        global ans
        ans = max(ans, eval(result))
        return

    # 괄호로 묶지 않는다. = 이전 + 다음    
    dfs(depth + 1, result + ops[depth] +nums[depth+1])

    # 괄호로 묶는다 = 이전 + 괄호 계산
    if depth + 1 < N//2:
        tmp = '(' + nums[depth+1] + ops[depth+1] + nums[depth+2] + ')'
        dfs(depth+2, result + ops[depth] + tmp)
    return


N = int(input())
expressions = input().rstrip()
nums = list(map(str, expressions[::2]))
ops = list(map(str, expressions[1::2]))

ans = -2**31
# dfs 1 런타임 방지용
if N == 1:
    print(nums[0])
else:
    dfs(0, nums[0])
    dfs(1, '('+nums[0]+ops[0]+nums[1]+')')
    print(ans)

'''
dfs(1, '('+nums[0]+ops[0]+nums[1]+')') 요게 핵심
처음을 괄호로 묶지 못한다는걸 괄호추가하기1에서는 왼쪽에서 계산하니까 인지를 못했었다.
테스트케이스 ㄳㄳ
'''