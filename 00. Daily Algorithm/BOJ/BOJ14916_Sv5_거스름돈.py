'''
무식하게
'''
import sys
input = sys.stdin.readline

n = int(input())
if n == 1 or n == 3:
    print(-1)
else:
    answer = n//5
    n -= 5*answer

    while n:
        if n < 0:
            answer -= 1
            n = n + 5
        else:
            answer += 1
            n = n - 2
    print(answer)

