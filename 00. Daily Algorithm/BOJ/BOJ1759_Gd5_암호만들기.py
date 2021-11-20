'''
백트래킹 접근
조건 : 최소 하나의 모음, 두개의 자음
'''
import sys
input = sys.stdin.readline

def backtrack(now, depth, p):
    result = []
    if depth == L:
        if len(set(p) & mothers) >= 1 and len (set(p) & sons) >= 2:
            return [''.join(p)]
    else:
        for i in range(now, C):
            result += backtrack(i+1, depth+1, p+[chars[i]])
    return result

L, C = map(int, input().split())
chars = sorted(input().split())

mothers = {'a', 'e', 'i', 'o', 'u'}
sons = set([x for x in chars if x not in mothers])

for answer in backtrack(0, 0, []):
    print(answer)