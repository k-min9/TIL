'''
배부른 마라토너 : https://www.acmicpc.net/problem/10546
'''

result = [0]*20
N = int(input())
for _ in range(2*N-1):
    names = input().rstrip()
    for i, n in enumerate(names):
        result[i] ^= ord(n)

print(''.join(map(chr, result)).rstrip())