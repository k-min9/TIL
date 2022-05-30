'''
괄호 = 스택 문제,
괄호 두 종류
'''
import sys
input = sys.stdin.readline

while True :
    words = input().rstrip()
    stack = []

    if words == "." :
        break

    for i in words:
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop()
            else : 
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
            
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')
        