'''
오늘은 별도의 알고리즘 특강도 있었고, 가볍게 쉬는 날로
'''
import sys
input = sys.stdin.readline

N = int(input())
answer = list()

for i in range(2, int(N**0.5)+1):
    while True:
        if N%i == 0:
            N /= i
            answer.append(i)
        else:
            break

if N != 1:
    answer.append(int(N))

print(*answer)

'''
무식하게 밀어붙이기~
'''