'''
두 유 노 딕셔너리?
'''

import sys
input = sys.stdin.readline

# 포켓몬 수, 문제 수
N, M = map(int, input().split())

# 번호도감, 이름도감
dic = dict()
nums = ['MissingNo']

for i in range(N):
    name = input().rstrip()
    dic[name] = i + 1
    nums.append(name)

for i in range(M):
    query = input().rstrip()
    # decimal : int형 변환 여부, digit: 숫자 모양, numeric : 연산 기호 포함 숫자 표현
    if query.isdigit():
        print(nums[int(query)])
    else:
        print(dic[query])


'''
포켓몬 번외 넘버링이 미싱노인건 국룰
'''