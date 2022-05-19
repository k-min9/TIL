'''
month to date를 잘해야 하고,
사용하는 양이 적어야 하는 회의실 문제
'''
import sys
input = sys.stdin.readline

# 상수
MD={1:0, 2:31, 3:59, 4:90, 5:120, 6:151, 7:181, 8:212, 9:243, 10:273, 11:304, 12:334}
def month_to_date(month, day):
    return MD[month]+day

flowers=list()

N=int(sys.stdin.readline())

for i in range(N):
    start_month, start_day, end_month, end_day=map(int, sys.stdin.readline().split())
    flowers.append((month_to_date(start_month, start_day), month_to_date(end_month, end_day)))

start=0
end=60

startdate=60  # 3월 1일
enddate=334  # 11월 30일
flowers.sort(key=lambda x:(x[0], x[1]))

x=-1
temp=0
changed=0
answer=list()
while end <= enddate and x < N:
    changed=0
    x+=1
    for i in range(x, N):
        # 회의실
        if flowers[i][0] > end:
            break
        if temp < flowers[i][1]:
            temp = flowers[i][1]
            x = i
            changed = 1

    if changed == 1:
        end=temp
        answer.append(flowers[x])
    else:
        answer=list()
        break
print(len(answer))
