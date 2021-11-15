'''
중복조합해도 되고, set 써도 되고...
'''
import sys
input = sys.stdin.readline

N = int(input())
answers = set()

for i in range(N+1):
    for j in range(N+1 - i):
        for k in range(N+1 -i-j):
            answers.add(i + 5*j + 10*k + 50*(N-i-j-k))

print(len(answers))