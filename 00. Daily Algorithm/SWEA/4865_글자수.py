import sys
from collections import Counter
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    # 중복제거
    str1 = set(input().rstrip())
    # 카운터
    str2 = Counter(input().rstrip())
    answer = 0
    for s in str1:
        answer = max(answer, str2[s])

    print(f'#{t + 1}', answer)
