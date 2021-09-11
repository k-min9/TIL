'''
연속된 k일 동안 2*n*k개 팔리고 단일 날짜 동안은 n개는 팔린 상품 중 제일 인기 있는 녀석
'''
from collections import Counter

def solution(research, n, k):

    answers = list()

    # 연속 검색일 기준, 검색 기준    
    group_n = len(research) - n + 1
    r_list = list()
    for i in range(group_n):
        counter = Counter(''.join(research[i:i+n]))
        for key, value in counter.items():
            if value >= 2*k*n:
                for r in research[i:i+n]:
                    if r.count(key) < k:
                        break
                else:
                    answers.append(key)
    answers.sort()

    if answers:
        answers = Counter(answers)
        return answers.most_common(1)[0][0]
    else:
        return "None"

print(solution(["abaaaa","aaa","abaaaaaa","fzfffffffa"], 2, 2)) # a
print(solution(["yxxy","xxyyy"], 2, 1)) # x
print(solution(["yxxy","xxyyy","yz"], 2, 1)) # y
print(solution(["xy","xy"], 1, 1)) # none