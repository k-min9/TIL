'''
재학생 k명이 반드시 포함되어야 하는 그룹 만들기 > 라이언
'''

def solution(student, k):
    
    # 재학생 수가 k명 이상인가
    if k > student.count(1):
        return 0
    
    answer = 0
    n = len(student)
    for i in range(n+1):
        for j in range(i+1):
            if k == student[j:i].count(1):
                answer += 1

    return answer


# # 그룹은 하나만, 투포인터
# def solution(student, k):
    
#     # 재학생 수가 k명 이상인가
#     if k > student.count(1):
#         return 0
    
#     # 변수 관리
#     left = 0
#     cnt = 0
#     answer = 0

#     for right, stu in enumerate(student):
#         if stu == 1:
#             cnt = cnt + 1
#         if cnt == k:
#             answer = answer + 1
#         # 왼쪽 포인터 이동
#         if cnt == k+1:
#             while left < right and student[left] == 0:  
#                 left += 1
#                 answer += 1



#print(solution([0,1,0,0], 1)) # 6
print(solution([0, 1, 0, 0, 1, 1, 0], 2)) # 8
print(solution([0,1,0,0], 2)) # 0