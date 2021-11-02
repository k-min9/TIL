'''
사람이 살 찌는게 전제에 기본 톤단위에서 놀지말라구... ㅠ
G가 10만이란건 N이 5만 이하라는거임(제곱간빼기 = 합차)
'''
import sys
input = sys.stdin.readline

# 몸무게 차이 = 100000이하의 자연수
G = int(input())

# 투 포인터
left = 1
right = 2
answers = list()
while left <= 50000:
    if right**2 - left**2 == G:
        answers.append(right)
    if right**2 - left**2 < G:
        right +=1
        continue
    left += 1

# 출력
if answers:
    for answer in answers:
        print(answer)
else:
    print(-1)