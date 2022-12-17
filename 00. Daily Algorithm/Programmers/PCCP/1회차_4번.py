# 운영체제
# 1. 받은 값 시간 순으로 나열
# 2. 시간 경과 시, 해당 시간에 포함되는 프로그램 나올때 까지 방출하여 힙에 넣기
# 3. 계산
from heapq import heappop, heappush

def solution(program):
    answer = [0]*11
    program = sorted(program, key=lambda x:-x[1])

    # 최초 힙 설정
    queue = []
    heappush(queue, program.pop())  # 순서 그대로 넣어도 됨   
    time_cur = queue[0][1]
    if program:
        while program[-1][1] <= time_cur:
            heappush(queue, program.pop())
            if not program:
                break

    while queue:
        score, time, cost = heappop(queue)

        answer[score] += (time_cur - time)
        time_cur += cost

        # 아직 모든 프로그램이 힙에 담기지 않음
        if program:
            # 힙이 비어있음
            if not queue:
                # 현재시간이 다음 프로그램 시작 전
                if time_cur < program[-1][1]:
                    time_cur = program[-1][1]
                    heappush(queue, program.pop())
            # 프로그램이 아직 비어있지 않음
            if program:
                while program[-1][1] <= time_cur:
                    heappush(queue, program.pop())
                    if not program:
                        break
    
    answer[0] = time_cur
    return answer
    
# [20, 5, 0, 16, 0, 0, 0, 0, 0, 0, 0]
# print(solution([[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]	))

# [19, 0, 0, 4, 3, 14, 0, 0, 0, 0, 0]
print(solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]))