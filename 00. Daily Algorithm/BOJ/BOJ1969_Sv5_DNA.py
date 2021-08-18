'''
접근 : Counter의 MostCommon 쓰고 싶어졌다.
'''

import sys
input = sys.stdin.readline
from collections import Counter

N, M = map(int, input().split())
dnas = [input().rstrip() for _ in range(N)]
# 여기서 비교대상을 묶는다.
dnas = list(zip(*dnas))

answer = 0
answer_dna = ''
for dna in dnas:
    c = Counter(dna)
    # 카운터(dic) 소트(숫자내림>사전오름)
    c = sorted(c.items(), key = lambda x: (-x[1], x[0]))
    answer_dna += c[0][0]
    answer += N - c[0][1]

print(answer_dna)
print(answer)

# 풀다보면 꼭 방향전환함. 그노무 사전식 정렬 진짜