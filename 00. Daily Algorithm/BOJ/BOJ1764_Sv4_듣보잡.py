import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = set(input().rstrip() for _ in range(N))
B = set(input().rstrip() for _ in range(M))
answers = sorted(list(A&B))
print(len(answers))
for answer in answers:
    print(answer)