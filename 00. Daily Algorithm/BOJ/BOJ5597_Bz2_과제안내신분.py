'''
입력하고 집합으로 뺄셈하고 소트하고 내고
'''
import sys
input = sys.stdin.readline

nums = set(int(input()) for _ in range(28))
alls = set(range(1,31))

answers = list(alls - nums)
answers.sort()

for answer in answers:
    print(answer)