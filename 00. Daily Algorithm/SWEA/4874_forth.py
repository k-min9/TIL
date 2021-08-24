import sys
sys.stdin = open('input.txt')


T = int(input())
for t in range(T):
    # 죄다 str로 받는다.
    formulas = list(input().split())
    
    # 계산합시당
    stack = []
    # try, except로 끝
    try:
        for formula in formulas:
            if formula == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif formula == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif formula == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
            elif formula == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(a//b)
            elif formula == '.':
                if len(stack) == 1:
                    print(f'#{t + 1}', *stack)
                else:
                    print(f'#{t + 1}', 'error')
            else:
                stack.append(int(formula))
    except:
        print(f'#{t + 1}', 'error')

