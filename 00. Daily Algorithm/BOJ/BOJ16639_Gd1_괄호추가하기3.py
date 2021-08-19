'''
네, 지금 알고리즘 인터뷰에서 배우는 부분이 분할정복입니다.
알고리즘 인터뷰 84. 괄호를 삽입하는 여러가지 방법 중에서 안 써본 방법 쪽으로 가져왔습니다.
문제 leetcode : https://leetcode.com/problems/different-ways-to-add-parentheses/ 
'''
import sys
input = sys.stdin.readline

def calc(input):
    return [a+b if c == '+' else a-b if c == '-' else a*b
            for i, c in enumerate(input) if c in '+-*'
            for a in calc(input[:i])
            for b in calc(input[i+1:])] or [int(input)]

N = int(input())
expressions = input().rstrip()
answers = calc(expressions)

print(max(answers))

# 예술적!

'''
import sys
import operator
input = sys.stdin.readline

def build(lo, hi):
    if lo == hi:
        return [nums[lo]]
    return [ops[i](a, b)
            for i in range(lo, hi)
            for a in build(lo, i)
            for b in build(i + 1, hi)]


N = int(input())
expressions = input().rstrip()
nums = list(map(int, expressions[::2]))
ops = list(map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, expressions[1::2]))

print(build(0, len(nums) - 1))

이거를 One-line 코드로 적은게 저 함수
'''