from collections import defaultdict

def solution(id_list, report, k):

     report = set(report)

     # 신고자 정리
     reported_list = defaultdict(int)     
     for r in report:
          reporter, reported = r.split()
          reported_list[reported] += 1

     # 최종 정리
     answers_list = list()
     for key, value in reported_list.items():
          if value >= k:
               answers_list.append(key)

     reporter_list = defaultdict(int) 
     for r in report:
          reporter, reported = r.split()
          if reported in answers_list:
               reporter_list[reporter] += 1

     answers = [0]*len(id_list)
     for i, id in enumerate(id_list):
          answers[i] = reporter_list[id]

     return answers


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)) # [2,1,1,0]
print(solution(["con", "ryan"], 	["ryan con", "ryan con", "ryan con", "ryan con"], 3)) # [0,0]