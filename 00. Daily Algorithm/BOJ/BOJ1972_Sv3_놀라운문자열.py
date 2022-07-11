'''
견적...도 필요 없이 그냥
구현만 하면 끝인데...?
'''
import sys
input = sys.stdin.readline

while True:
    words = input().strip()
    if words == '*':
        break

    N = len(words)
    flag = True
    for i in range(N-1):
        tmp = set()
        for j in range(N-1-i):
            tmp.add(words[j]+words[j+i+1])
        if len(tmp) != N-1-i:
            flag = False
            break
    
    if flag:
        print(words + ' is surprising.')
    else:
        print(words + ' is NOT surprising.')

'''
...끝!
'''