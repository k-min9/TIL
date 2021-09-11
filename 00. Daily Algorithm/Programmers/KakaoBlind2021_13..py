from collections import defaultdict
from math import ceil

def solution(fees, records):
     # 문자열 시간을 받아 정수 분으로 변경
     def time_convert(time):
          h, m = map(int, time.split(':'))
          return h * 60 + m

     # 총 시간을 받아 운전료로 변경
     def calc_fee(time):
          if time <= fees[0]:
               return fees[1]
          else:
               return fees[1] + ceil((time - fees[0])/fees[2])*fees[3]

     #key 차 번호, value 입차 시간
     park_cur = defaultdict(int)
     #key 차 번호, value 총 주차시간
     park_all = defaultdict(int)

     for record in records:
          time, car_num, status = record.split()
          if status == 'IN':
               park_cur[car_num] = time_convert(time)
          else:
               park_all[car_num] += (time_convert(time) - park_cur[car_num])
               del park_cur[car_num]

     # 남아 있는 차는 23:59(1439에 아웃)
     if park_cur:
          for key, value in park_cur.items():
               park_all[key] += 1439 - value

     # 차량 번호 순 정렬
     park_all = sorted(park_all.items())

     # 청구 요금 정산
     answers = list()
     for car_num, park_time in park_all:
          answers.append(calc_fee(park_time))
     
     return answers
               

# 출력 되는게 답임
print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))