'''
시간 빼기 하는 법 연습
'''
from datetime import datetime
import sys
input = sys.stdin.readline

for _ in range(3):
    a, b  = input().split()
    before = datetime.strptime(a, "%H:%M:%S")
    after = datetime.strptime(b, "%H:%M:%S")
    answer = (after - before).seconds
    print(answer)




# 실제 풀이
import datetime
from datetime import timedelta

for i in range(3):
    start,end=input().split()

    st=int(start.replace(":",""))
    ed=int(end.replace(":",""))

    stH,stM,stS=map(int,start.split(":"))
    edH,edM,edS=map(int,end.split(":"))

    stime=datetime.datetime(2021,1,1,stH,stM,stS)

    tmp_time=stime.strftime('%H%M%S')

    cnt=0
    if int(tmp_time)%3==0:
            cnt+=1
    etime=datetime.datetime(2021,1,1,edH,edM,edS)
    etime=etime.strftime('%H%M%S')

    while True:
        if tmp_time==etime:
            break
        
        stime=stime+timedelta(seconds=1)  # 1초씩 더하기
        tmp_time=stime.strftime('%H%M%S')
        if int(tmp_time)%3==0:
            cnt+=1

    print(cnt)