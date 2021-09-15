'''
딕셔너리 + XOR
'''
import sys
input = sys.stdin.readline

answer = 0
cows = dict()
for _ in range(int(input())):
    cow, pos = map(int, input().split())
    cow = str(cow)
    if cow in cows and cows[cow] != pos:
        answer += 1
    cows[cow] = pos
print(answer)