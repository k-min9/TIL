'''
ord chr 음 replace?
'''
import sys
input = sys.stdin.readline

N = int(input())
expression = list(input().rstrip())
num = [int(input()) for _ in range(N)]

stack=list()

for i in expression:
    if i.isalpha():
        stack.append(num[ord(i)-ord('A')])
    else:
        a=stack.pop()
        result=stack.pop()

        if i=='+':
            result+=a

        elif i=='-':
            result-=a

        elif i=='*':
            result*=a

        elif i=='/':
            result/=a

        stack.append(result)

print('%.2f' %stack[-1])

'''
애초에 표기식이니까 그냥 쌓으면 됨...!
'''