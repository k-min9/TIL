'''
모든 문자열은 1이상 20이하의 알파벳 소문자로 이루어져있으며 같은 이름을 가진 의상은 존재하지 않는다. < 난이도 떨어지는 소리
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):

    n = int(input())
    answers = defaultdict(int)
    for _ in range(n):
        trash, category = input().split()
        answers[category] += 1
    
    answer = 1
    for k, v in answers.items():
        answer *= (v + 1)
    answer -= 1
    print(answer)
