'''
진짜 오랜만의 브론즈 문제지만, 카운터 쓸 수 있는 것 같아서!
'''
from collections import Counter
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = Counter(input().replace(' ','').strip())
    if len(a)> 1:
        if a.most_common(2)[0][1] > a.most_common(2)[1][1]:
            print(a.most_common(2)[0][0])
        else:
            print('?')
    else:
        print(a.most_common(1)[0][0])
    
'''
재밌는 풀이덕에 평소보다 2배는 걸린거 같은데...
'''