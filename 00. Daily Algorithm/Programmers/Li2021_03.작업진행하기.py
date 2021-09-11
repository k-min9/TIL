'''
작업을 순서대로 진행하자
'''
from collections import defaultdict, Counter

def solution(jobs):
    # time 까지 들어온 작업 분류
    def jobs_in(jobidx):    
        for i in range(jobidx, n):
            if jobs[i][0] <= time_end:
                # 걸리는 시간, 중요도 추가
                jobs_next[str(jobs[i][2])] += jobs[i][1]
                jobs_important[str(jobs[i][2])] += jobs[i][3]
                jobidx = jobidx + 1
        return jobidx
        
    n = len(jobs)
    # 1번 일 넣고, 걸리는 시간, 중요도 dict
    jobs_next = defaultdict(int)
    jobs_important = Counter()
    jobs_next[str(jobs[0][2])] += jobs[0][1]
    jobs_important[str(jobs[0][2])] += jobs[0][3]

    # 초기 시간, 다음 정리 일 번호
    time = jobs[0][0]  
    jobidx = 1

    answers = list()
    while True:
        # 일 안 끝났는데 현재 일이 없으면 다음 시간까지 땡겨서
        if not jobs_important and jobidx != n:
            time_end = jobs[jobidx][0]
            # 기존 것과 같으면 삭제
            if jobs[jobidx][2] == answers[-1]:
                answers.pop()
            jobidx = jobs_in(jobidx)


        # 다음 일 선정 (중요도에서 분류 뽑기)
        job_cur = sorted(jobs_important.items(), key=lambda x: (-x[1], x[0]))[0][0]
        del jobs_important[job_cur]

        # 걸릴 시간
        job_time = jobs_next[job_cur]
        del jobs_next[job_cur]

        time_end = time + job_time

        # 그 사이에 일 추가
        jobidx = jobs_in(jobidx)

        # 일 종료
        time = time_end

        # 같은 분류 일이 남아 있는 한 작업 이어짐
        while job_cur in jobs_important:
            del jobs_important[job_cur]
            job_time = jobs_next[job_cur]
            del jobs_next[job_cur]
            time_end = time + job_time
            jobidx = jobs_in(jobidx)
            time = time_end


        
        answers.append(int(job_cur))

        if len(jobs_next) == 0 and jobidx == n:
            break

    return answers

print(solution([[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]])) # [2, 1, 2, 3]
print(solution([[1, 2, 1, 5], [2, 1, 2, 100], [3, 2, 1, 5], [5, 2, 1, 5]])) # [1, 2]
print(solution([[0, 2, 3, 1], [5, 3, 3, 1], [10, 2, 4, 1]])) # [3, 4]
print(solution([[0, 5, 1, 1], [2, 4, 3, 3], [3, 4, 4, 5], [5, 2, 3, 2]])) # [1, 3, 4]