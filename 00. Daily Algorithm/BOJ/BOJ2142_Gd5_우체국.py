'''
소금물?
'''
# import sys
# input = sys.stdin.readline
# from bisect import bisect_right

# N = int(input())
# sums = 0
# population = list()
# populations = 0
# for _ in range(N):
#     x, a = map(int, input().split())
#     sums += a * x
#     population.append(x)
#     populations += x

# answer = sums//populations
# if sums % populations > populations // 2:
#     answer = answer + 1
# idx = max(bisect_right(population, answer)-1 , 0)
# print(population[idx])

'''
아니었고, 인구수가 절반이 되는 마을
'''

import sys
input = sys.stdin.readline

towns = list()
populations = 0
for i in range(int(input())):
    x, a = map(int, input().split())
    towns.append((x, a))
    populations += a

towns.sort()
populations /= 2

for x, a in towns:
    populations -= a
    if populations<=0:
        print(x)
        break