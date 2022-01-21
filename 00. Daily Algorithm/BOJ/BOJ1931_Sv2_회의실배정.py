'''
제출이 10만이 넘어가는 문제를 이제야 풀다니 ㅋㅋㅋ
아마 리트코드로 풀기는 했을듯 함
'''
import sys
input = sys.stdin.readline

N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]
schedules.sort(key=lambda x: (x[1], x[0]))


answer = 0
endtime = 0
for start, end in schedules:
    if start >= endtime:
        answer += 1
        endtime = end

print(answer)