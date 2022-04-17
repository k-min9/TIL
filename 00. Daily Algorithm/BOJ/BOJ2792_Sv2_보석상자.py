'''
이분 탐색 많네 요즘
'''
import sys
input = sys.stdin.readline

# 입력 (아이들 수, 책상 수)
N, M = map(int, input().split())
gems = [int(input()) for _ in range(M)]

# start, end 초기화
start = 1
end = sum(gems)

# 이진 탐색
answer = 0
while start <= end:
    
    mid = (start + end) // 2
    
    # 보석받은 학생 수
    num_student = 0
    for num_gem in gems:
        if num_gem % mid > 0:
            num_student += num_gem // mid + 1
        else:
            num_student += num_gem // mid

    if num_student > N:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid
        
print(answer)
