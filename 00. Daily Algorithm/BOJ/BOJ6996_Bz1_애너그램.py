'''
감상 : 인풋받고, 소트하고, 비교하고
'''

n = int(input())

for _ in range(n):
    a,b = input().split()
    if sorted(a) == sorted(b):
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')
