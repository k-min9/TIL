'''
엄청 비슷한? 줄 길이 문제를 본거 같은...데?
'''
import sys
input = sys.stdin.readline


def chk(length):
    cnt = 0
    for pa in pas:
        cnt += pa//length
    if cnt >= C:
        return True
    return False


# 파의 갯수와 파닭 수
S, C = map(int, input().split())
pas = [int(input()) for _ in range(S)]

start = 1
end = max(pas)
answer = (start+end)//2
while start <= end:
    mid = (start+end)//2
    if chk(mid):
        start = mid+1
        answer = mid
    else:
        end = mid-1
answer = sum(pas) - answer*C

print(answer)
