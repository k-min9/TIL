'''
DP
'''
import sys
input = sys.stdin.readline

fibos = [0, 1]
for _ in range(10001):
    fibos.append(fibos[-1] + fibos[-2])
print(fibos[int(input())])

'''
쉬어가는날!
'''