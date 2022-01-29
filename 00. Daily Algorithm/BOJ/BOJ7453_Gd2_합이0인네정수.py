'''
a+b / c+d 로 분할 정복하면 O(N^4)가 N^2가 된다
이때 값을 key 그 숫자를 가지는 조합수를 value로 하는 dictionary 쓰면...?
아주 그냥 개껌이죠!
'''
import sys
input = sys.stdin.readline
from collections import defaultdict

a_list, b_list, c_list, d_list = list(), list(), list(), list()
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)
    d_list.append(d)

dict_1 = defaultdict(int)
for a in a_list:
    for b in b_list:
        dict_1[a+b] += 1

answer = 0
for c in c_list:
    for d in d_list:
        tmp = -(c+d)
        if tmp in dict_1:
            answer += dict_1[tmp]

print(answer)

'''
껌...은 아니었고 defaultdict가 그냥 dict보다 조ㅡ금 더 느리네
'''
