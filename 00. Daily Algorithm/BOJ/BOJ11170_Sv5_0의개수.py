'''
T20에 N이 백만이면 그냥 세도 되지 않나...?
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    answer = 0
    N, M = map(int, input().split())
    for i in range(N, M+1):
        answer += str(i).count('0')
    print(answer)