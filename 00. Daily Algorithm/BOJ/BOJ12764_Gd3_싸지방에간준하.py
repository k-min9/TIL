'''
회의실 문제
오늘은 코테 전 몸풀이라 참조만 했습니다. : https://deok2kim.tistory.com/326
'''
import sys
import heapq
input = sys.stdin.readline

N = int(input())
logs = [list(map(int, input().split())) for _ in range(N)]
logs.sort()  # 시작이 빠른 순으로 정렬

# 자리 카운트 셀 것
use_cnt = [0] * N
use_cnt[0] = 1

# 사용중인 컴퓨터 끝나는시간과 자리 번호
pq = []
heapq.heappush(pq, [logs[0][1], 0])  

# 남아있는 가장 자리들 ( 앞자리 뽑으려고 ) 
computers_pq = [i for i in range(N)]
heapq.heapify(computers_pq)  # 자리만
heapq.heappop(computers_pq)

for log in logs[1:]:  # 이미 넣었으니까 1부터 시작
    start, end = log

    if pq[0][0] > start:  # 제일빨리 끝나는 애보다 시작 시간이 늦으면 남아 있는 다른 자리로 가라
        new_posi = heapq.heappop(computers_pq)
        use_cnt[new_posi] += 1
        heapq.heappush(pq, [end, new_posi])
    else:
        while True:  # 사용중인 자리가 여러군데가 끝나있는 경우가 있다. 그 중에서 가장 앞선 자리를 뽑아야한다.
            prev_end, prev_seq = heapq.heappop(pq)
            if pq and pq[0][0] <= start:  # 그 다음 것도 이미 끝나있는 경우가 있다.
                heapq.heappush(computers_pq, prev_seq)
                continue
            else:
                new_posi = heapq.heappushpop(computers_pq, prev_seq)
                heapq.heappush(pq, [end, new_posi])
                use_cnt[new_posi] += 1
                break

idx = N - use_cnt.count(0)
print(idx)
print(*use_cnt[:idx])
# print(' '.join(list(map(str, use_cnt[:idx]))))