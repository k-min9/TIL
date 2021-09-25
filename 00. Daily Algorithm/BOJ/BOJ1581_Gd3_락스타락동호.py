'''
일단 전개해보자
'''

import sys
input = sys.stdin.readline

FF, FS, SF, SS = map(int, input().split())

if FF == 0 and FS == 0:
    print(SS + min(SF, 1))
elif FS == 0:
    print(FF)
else:
    if FS <= SF:
        print(FF+SS+2*FS)
    else:
        print(FF+SS+2*SF+1)
    


