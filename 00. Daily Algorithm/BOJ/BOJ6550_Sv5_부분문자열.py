'''
문자열 제어는 특기라고 말하고 싶었는데 으음, 얘는 아닌거 같은데
'''
import sys
input = sys.stdin.readline


def solution(s, t):
    si = 0

    for ti in range(len(t)):
        if t[ti] == s[si]:
            si += 1
            if si == len(s):
                return 'Yes'
    return 'No'

while True:
    try:
        s, t = input().split()
        print(solution(s, t))
    except:
        break