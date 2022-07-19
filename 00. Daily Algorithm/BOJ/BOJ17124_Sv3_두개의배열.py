'''
B에 있는 값중 A[i]에 가까운 값이 C[i]가 된다.
왼쪽에서 bisect, 오른쪽에서 bisect 절대값이 작은 쪽이 답임
>> 왼쪽에서만 하면 되지 않나...?
'''
import sys
input = sys.stdin.readline
from bisect import bisect_left

for _ in range(int(input())):
    n, m = map(int, input().split())  # A와 B의 길이
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort()

    answers = list()
    for a in A:
        
        l = bisect_left(B, a)
        if l >= m:
            answers.append(B[-1])  # 못찾으면 맨 끝
            continue
            
        if abs(B[l-1]-a) <= abs(B[l]-a):
            answers.append(B[l-1])
        else:
            answers.append(B[l])

    print(sum(answers))    

