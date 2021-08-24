import sys
sys.stdin = open('input.txt')

from collections import defaultdict

for t in range(1, 11):
    dump = int(input())
    dic = defaultdict(int)
    for box in list(map(int, input().split())):
        dic[box] += 1
    for i in range(dump):
        max_height = max(dic)
        min_height = min(dic)
        dic[max_height] -= 1
        dic[max_height-1] += 1
        dic[min_height] -= 1
        dic[min_height+1] += 1
        if dic[max_height] == 0:
            del(dic[max_height])
            max_height -= 1
        if dic[min_height] == 0:
            del (dic[min_height])
            min_height += 1

    print(f'#{t}', max_height - min_height)

