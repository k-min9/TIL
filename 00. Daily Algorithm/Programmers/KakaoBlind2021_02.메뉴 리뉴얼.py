from collections import Counter
from itertools import combinations

def solution(orders, course):
    course_selected = list()
    for c in course:
        course_list = list()
        for order in orders:
            for combs in combinations(sorted(order), c):
                course_list.append(combs)
        counter = Counter(course_list)
        if counter:
            max_value = counter.most_common(1)[0][1]
        else:
            max_value = 0
        if max_value >= 2:
            for key, value in counter.items():
                if value == max_value:
                    course_selected.append(key)

    answer = list()
    for c in course_selected:
        answer.append(''.join(c))
    
    answer.sort()
    
    return answer

'''
간단해 보이고 짧아 보이는 풀이지만 몇번이나 걸려넘어짐
1. 문제를 잘못 이해하고 코스길이? 당 가장 제일 잘 팔리는 목록을 짜라는 말을 늦게나 이해함 
> 처음에 for order  순으로 접근했다가 for c in course 순으로 크게 뒤집어야 했음. 문제를 잘 읽자.
2. sort 어디에 집어 넣나 할때 콤비네이션 직전에 집어 넣으면 order가 언팩되면서 정렬된다는거 깨달음.
3. index out of list 뜸 이게 VS code에서는 답이 나온 상황에서 뜬거라 조금 당황, 
별 거 아니고 카운터가 빈 값일때 VScode는 걍 넘어가고, 프로그래머스는 에러 띄움
index out of list 뜨면 중간 과정 print 내용물 전혀 못봐서 디버깅이 안된다는것도 깨달음
'''