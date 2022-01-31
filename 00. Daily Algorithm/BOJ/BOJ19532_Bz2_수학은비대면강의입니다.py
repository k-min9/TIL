'''
유일해 존재한다고 알려주면 오버플로우도 없는 파이썬에게는 너무 상황이 좋지 않낭
'''

import sys
input = sys.stdin.readline

a,b,c,d,e,f=map(int,input().split())
x = (c*e-b*f)//(a*e-b*d)
y = (c*d-a*f)//(b*d-a*e)
print(x, y)

'''
오늘은 올솔이어서 브론즈! 풀은거라구!
'''