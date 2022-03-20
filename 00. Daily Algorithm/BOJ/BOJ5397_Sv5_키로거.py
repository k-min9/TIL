'''
스택 문제가 가끔 희안할때도 있긴 한데...
우클릭시 문자열 입력후 합칠걸 right에 저장해둔다.
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    strs = input().rstrip()
    # 스택 2개
    left = list()
    right = list()
    for str in strs:
        if str == '<':
            if left:
                right.append(left.pop())
        elif str == '>':
            if right:
                left.append(right.pop())
        elif str == '-':
            if left:
                left.pop()
        else:
            left.append(str)
    left.extend(reversed(right))
    print(''.join(left))
