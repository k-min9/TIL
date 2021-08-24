import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    words = input().rstrip()
    stack = list()
    paren = set(['{', '}', '(', ')'])

    answer = 1
    for word in words:
        if word in paren:
            if word == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    answer = 0
            elif word == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    answer = 0
            else:
                stack.append(word)
    if stack:
        answer = 0

    print(f'#{t+1}', answer)
