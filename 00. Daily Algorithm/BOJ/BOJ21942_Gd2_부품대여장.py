'''
토스뱅크 코딩 테스트 본 이후 느낀건 datetime 포맷에 익숙해져야 한다는 거였는데,
적절한 타이밍에 적절한 문제가 나왔다.
다만 풀이는 외부 참조 따라치기 : https://welog.tistory.com/330
'''
from datetime import datetime
from collections import defaultdict
import sys
input = sys.stdin.readline
 
def convert(L):
    day,arg = L.split('/')
    day = int(day)
    hour,min = map(int,arg.split(':'))
    total_min = min + hour*60 + day*24*60
    return total_min
 
N,L,F = list(input().split())
N = int(N)
F = int(F)
L = convert(L)
part_manager_dict = defaultdict(dict)
 
tardy_dict = defaultdict(int)
for _ in range(N):
    total_string = input()
    time_string = total_string[:16]
    time_S = datetime.strptime(time_string,'%Y-%m-%d %H:%M')
    part_name,person = total_string[16:].split()
    if part_manager_dict[person].get(part_name):
        borrowed_time = time_S - part_manager_dict[person][part_name]
        day = borrowed_time.days
        min = borrowed_time.seconds//60
        to_time = day*60*24 + min
        if to_time > L:
            tardy_dict[person] += (to_time-L)*F
        del part_manager_dict[person][part_name]
    else:
        part_manager_dict[person][part_name] = time_S
 
 
if len(tardy_dict.keys()):
    key_list = sorted(tardy_dict.keys())
 
    for key in key_list:
        print(key,int(tardy_dict[key]))
 
else:
    print(-1)

'''
datetime은 잘못사용하면 시간초과가 나나보다. 헤ㅡ 그렇구나
근데 대용법이 없으니 뭐 음...
'''