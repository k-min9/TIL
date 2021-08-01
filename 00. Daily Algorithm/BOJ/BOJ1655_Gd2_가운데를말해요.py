'''
0.1초 = 자료구조를 쓰지 않는다면 당신의 답안을 죽이겠다.
'''

import sys
input = sys.stdin.readline
from heapq import heappop, heappush

# heap 두개 사용 비교에 쓰인다
min_heap = []  # 중앙값 보다 큰 걸 최소heap에 넣고 가장 작은값을
max_heap = []  # 중앙값 보다 같거나 작은 걸 최대heap에 넣고 가장 큰 값을 <= 답은 여기서 뽑아야한다.

N = int(input())

for i in range(N):
    n = int(input())

    # 교대로 넣기, (출력이 나오는 max먼저)
    if i%2==0:
        heappush(max_heap, -n)
    else:
        heappush(min_heap, n)
    
    # 이제 전제 조건에 부합하지 않을 경우 min max 장소를 바꿈. 
    # i=0 일때는 참조할게 없어서 에러
    if i>=1 and -max_heap[0]>min_heap[0]:
        a = -heappop(max_heap)
        b = heappop(min_heap)
        heappush(min_heap,a)
        heappush(max_heap,-b)

    print('heap', min_heap, max_heap)
    print(-max_heap[0])
    
'''
오늘 할 스터디 내용이 스택, 큐, 데크, 우선순위 큐 였는데 
백준 추천 문제가 우선순위 큐 엌ㅋㅋ
'''
        
