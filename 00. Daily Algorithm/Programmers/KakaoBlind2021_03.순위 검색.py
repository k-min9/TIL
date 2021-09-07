'''
1차시도 > 투포인터 = 실패
실패 눈치 챈 시점 : sort 해도 언어 미선택 백엔드 선택시 사이에 구멍 생김
'''

# def solution(info, query):
#     n = len(info)
#     for i in range(n):
#         info[i] = info[i].split()
#     info.sort()
#     for i in info:
#         print(*i)
    

#     for q in query:
#         q = q.split(' ')
#         # 나눌 필요 없음, 걍 and가 빠진 만큼 출력이 이쁨
#         q = q+[q[-1]]
#         q = q[0:9:2]
        
#         # query의 변수명이 queries면 더 좋았을뻔 했는데
#         # 풀이는 투포인터(변수 숫자 5만)
#         l, r = 0, n-1
#         for i in range(4):
#             if q[i] == '-':
#                 continue
#             # 왜 안 while?
#             for j in range(l,r+1):
#                 # 빠르게 하려면 여기서 bisect겠네
#                 if q[i] == info[j][i]:
#                     l = j
#                     break
#             else:
#                 #print('여기서 브레이크하면 어디감')
#                 break
#             for j in range(r,l-1,-1):
#                 if q[i] == info[j][i]:
#                     r = j
#                     break
#             print('pi', l, r)
            
#         #print('여기요')
#         answers = list()
#         for i in range(l, r+1):
#             answers.append(info[i][4])
#         answers.sort()
#         print(answers)


#         print(q)

'''
2차시도 : 총 3*2*2*2의 리스트로 쪼개서 저장하면 된다고 생각하게 됨. 조립식 합체로봇
[언어][지원][경력][푸드]
'''

# 상수
set_query1_A = {0,1,2,3,8,9,10,11,16,17,18,19}
set_query1_B = {4,5,6,7,12,13,14,15,20,21,22,23}
set_query2_A = {0,1,4,5,8,9,12,13,16,17,20,21}
set_query2_B = {2,3,6,7,10,11,14,15,18,19,22,23}
set_query3_A = {0,2,4,6,8,10,12,14,16,18,20,22}
set_query3_B = {1,3,5,7,9,11,13,15,17,19,21,23}

def solution(info, query):
    n = len(info)
    for i in range(n):
        info[i] = info[i].split()
        
    # 24개 그룹 생성 예정
    groups = [[] for _ in range(24)]
    for i in info:
        # 언어 체크(cpp, java, python)
        if i[0] == 'cpp':
            j = 0
        elif i[0] == 'java':
            j = 8
        else:
            j = 16
        # 지원 체크(back, front)
        if i[1] == 'frontend':
            j = j + 4
        # 경력 체크(senior, junior)
        if i[2] == 'junior':
            j = j + 2
        # 푸드 체크 (chicken, pizza)
        if i[3] == 'pizza':
            j = j + 1
        groups[j].append(int(i[4]))  
  

    # 답 담을 리스트
    answers = list()
    # 이제 나눠보자
    for q in query:
        # 쿼리 리스트 화
        chk = q.split(' ')
        # 언어 체크(cpp, java, python)
        if chk[0] == 'cpp':
            query_num = set(range(0,8))
        elif chk[0] == 'java':
            query_num = set(range(8,16))
        elif chk[0] == 'python':
            query_num = set(range(16,24))
        else:
            query_num = set(range(0,24))
        # 지원 체크(back, front)
        tmp = set()
        if chk[2] == 'backend':
            query_num = query_num & set_query1_A               
        elif chk[2] == 'frontend':
            query_num = query_num & set_query1_B  
        # 경력 체크(senior, junior)
        if chk[4] == 'senior':
            query_num = query_num & set_query2_A             
        elif chk[4] == 'junior':
            query_num = query_num & set_query2_B 
        # 푸드 체크 (chicken, pizza)
        if chk[6] == 'chicken':
            query_num = query_num & set_query3_A             
        elif chk[6] == 'pizza':
            query_num = query_num & set_query3_B
                    
        # print('q', query_num)
        answer = 0
        for num in query_num:
            for g in groups[num]:
                if g >= chk[7]:
                    answer + 1
        answer.append(answer)

    return answers



solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])


'''
효율성 테스트??????????
'''

from bisect import bisect_left

bisect_left()