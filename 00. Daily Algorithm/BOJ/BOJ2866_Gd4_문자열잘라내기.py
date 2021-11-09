'''
R, C가 1000이하인데 이분탐색 필요한가?? 진짜로??
'''
# import sys
# input = sys.stdin.readline

# R, C = map(int, input().split())
# strings = [list(input().rstrip()) for _ in range(R)][::-1]

# answer = 0 
# while True:
#     strings.pop()
#     if len(set(zip(*strings))) != C:
#         break
#     answer += 1
# print(answer)

'''
필요하네 >> 2차 도전
'''
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
strings = [list(input().rstrip()) for _ in range(R)][::-1]

answer = 0
lo = 0
hi = R-1
while lo<=hi:
    mid = (lo+hi)//2
    if len(set(zip(*strings[:(mid+1)]))) == C:
        # 중복 미 발생
        answer = mid
        hi = mid-1
    else:
        # 중복 발생
        lo = mid+1


print(R-1-answer)