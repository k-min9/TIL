'''
카운터 교집합?
'''
from collections import Counter

while True:
    try:
        a = input().rstrip()
        b = input().rstrip()
    except:
        break

    answers = Counter(a) & Counter(b)

    # 카운터 정렬 > 리턴 : 리스트
    answers = sorted(answers.items())
    
    answer = ''
    for k, v in answers:
        answer += k*v
    print(answer)

'''
input = sys.stdin.readline 떼고 풀어야 한다.
'''
