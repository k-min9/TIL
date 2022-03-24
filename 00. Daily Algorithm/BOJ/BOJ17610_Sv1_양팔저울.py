'''
SWEA에서 비슷한 문제 본거 같은데...
'''
import sys
input = sys.stdin.readline


# 입력
K = int(input())
weights = list(map(int, input().split()))
weights.sort()
S = sum(weights)

answers = set()
answers.add(weights[0])
for i in range(1, K):
    cur = weights[i]
    temp = set()
    temp.add(cur)

    for answer in answers:
        temp.add(cur + answer)
        temp.add(abs(cur - answer))
    
    answers = answers | temp

if 0 in answers:
    answers.remove(0)

print(S - len(answers))
