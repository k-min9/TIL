'''
간단한 DP 문제
'''
import sys
input = sys.stdin.readline

N = int(input())
grpahs = []

for i in range(N):
    grpahs.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            grpahs[i][j] = grpahs[i][j] + grpahs[i-1][j]
        elif i == j:
            grpahs[i][j] = grpahs[i][j] + grpahs[i-1][j-1]
        else:
            grpahs[i][j] = max(grpahs[i-1][j-1], grpahs[i-1][j]) + grpahs[i][j]

print(max(grpahs[N-1]))