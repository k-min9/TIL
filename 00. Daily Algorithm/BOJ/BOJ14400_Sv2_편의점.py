'''
맨하튼 거리를 직접 구해보자...?
'''
import sys
input = sys.stdin.readline

N = int(input())
x_list = list()
y_list = list()
x_sums, y_sums = 0, 0
for _ in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    x_sums += x
    y_list.append(y)
    y_sums += y

x_list.sort()
y_list.sort()

x_place = x_list[(N-1)//2]
y_place = y_list[(N-1)//2]

answer = 0
for x in x_list:
    answer += abs(x-x_place)
for y in y_list:
    answer += abs(y-y_place)

print(answer)

'''
처음에 round로 허공에 세웠는데 그런 문제가 아니여서 오래 걸림;;;
'''