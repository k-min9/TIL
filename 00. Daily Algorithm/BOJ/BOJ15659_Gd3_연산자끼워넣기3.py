'''
~from BOJ 14888 의 상위 문제
연산 순서로 계산하는게 중요
...eval 쓰면 되지 않아?
'''
# import sys
# input = sys.stdin.readline
# from itertools import permutations

# N = int(input())
# nums = list(input().split())
# opers = list()
# a, b, c, d = map(int, input().split())

# for _ in range(a):
#     opers.append('+')
# for _ in range(b):
#     opers.append('-')
# for _ in range(c):
#     opers.append('*')
# for _ in range(d):
#     opers.append('//')

# answer_min = 1000000000
# answer_max = -1000000000

# for p in permutations(opers, N-1):
#     expression = nums[0]
#     for i in range(1, N):
#         expression += p[i-1]
#         expression += nums[i]
#     exp = eval(expression)
#     answer_max = max(answer_max, exp)
#     answer_min = min(answer_min, exp)

# print(answer_max)
# print(answer_min)

'''
네 시간초과. 성실히 합시다 성실히
'''
import sys
input = sys.stdin.readline

def dfs(exp, idx):

    global answer_min
    global answer_max

    if idx == n-1:
        answer = eval(exp)
        answer_min = min(answer_min, answer)
        answer_max = max(answer_max, answer)
        return 
    
    for i in range(4):

        if opers[i] == 0:
            continue
        if i == 0:
            exp_next = exp + '+' + numbers[idx+1]
        elif i == 1:
            exp_next = exp + '-' + numbers[idx+1]
        elif i == 2:
            exp_next = exp + '*' + numbers[idx+1]
        else:
            exp_next = exp + '//' + numbers[idx+1]
        opers[i] = opers[i] - 1
        dfs(exp_next, idx+1)
        opers[i] = opers[i] + 1

#Min, Max
answer_min = 1000000001
answer_max = -1000000001 

#실행
n = int(input())
numbers = list(input().split())
opers = list(map(int, input().split()))

dfs(numbers[0], 0)

print(answer_max)
print(answer_min)