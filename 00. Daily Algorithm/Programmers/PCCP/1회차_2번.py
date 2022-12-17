# 체육대회
# N=100 > 맘대로 풀어라
from itertools import permutations

def solution(ability):
    num_student = len(ability)
    num_subject = len(ability[0])

    answer = 0
    for students in permutations(range(num_student), num_subject):
        subject = 0
        tmp = 0
        for student in students:
            tmp += ability[student][subject]
            subject += 1
        answer = max(answer, tmp)

    return answer

# 210
print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))

# 60
print(solution([[20, 30], [30, 20], [20, 30]]))