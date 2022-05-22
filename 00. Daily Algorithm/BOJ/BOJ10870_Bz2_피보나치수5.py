'''
인턴 첫날! ㅎㅎ! 가벼운 도토리 풀이!
'''

import sys
input = sys.stdin.readline

fibos = [0, 1]
for _ in range(21):
    fibos.append(fibos[-1] + fibos[-2])
print(fibos[int(input())])