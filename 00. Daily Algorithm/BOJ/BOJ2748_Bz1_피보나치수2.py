'''
DP
'''
import sys
input = sys.stdin.readline

fibos = [0, 1]
for _ in range(90):
    fibos.append(fibos[-1] + fibos[-2])
print(fibos[int(input())])

'''
프로젝트 마지막 전 기분전환! 다들 파이팅!
'''