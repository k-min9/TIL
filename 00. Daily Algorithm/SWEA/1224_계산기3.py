import sys
sys.stdin = open('input.txt')


def make_postfix(formulas):
    stack = []
    postfix = []

    # 우선순위 dic
    priority = {'+': 1, '*': 2, '(': 0}

    for i in formulas:
        # 알파벳은 숫자 스택
        if i.isdigit():
            postfix.append(i)
        # 여는 괄호는 연산자 스택
        elif i == '(':
            stack.append(i)
        elif i == ')':
            # 연산자 스택이 비거나 여는 괄호를 만날 때 까지 pop
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            # 마지막 pop은 여는 괄호 또는 None이므로 저장하지 않는다
            stack.pop()
        # 연산자는 연산자 스택
        else:
            # 현재 연산자가 스택의 top 연산자보다 우선순위가 높은 경우
            while stack and priority[i] < priority[stack[-1]]:
                postfix.append(stack.pop())
            # 그렇지 않은 경우거나 낮은 우선순위를 가진 연산자를 모두 pop한 경우
            stack.append(i)

    # 남은 연산자 스택을 죄다 표기로 이동
    while stack:
        postfix.append(stack.pop())

    # 정답 출력
    return ''.join(postfix)


for t in range(10):
    # 바로 후위로 바꾸고
    n = int(input())
    formulas = make_postfix(input().rstrip())
    
    # 계산합시당
    stack = []
    # 파이썬은 그냥 문자열을 배열처럼 써도 되니까
    for formula in formulas:
        if formula == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a+b)
        elif formula == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a*b)
        else:
            stack.append(int(formula))

    print(f'#{t+1}', *stack)
