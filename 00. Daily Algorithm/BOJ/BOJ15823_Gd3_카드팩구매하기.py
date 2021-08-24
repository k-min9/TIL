'''
접근 : 멍하다. 뭐임 이 문제. N이 10만이니까 견적은 O(NlogN). 
일단 떠오르는건 투 포인터 + 슬라이딩 윈도우 인데 중복 선택 불가가 방해되나?? 견적내로 안 될 듯
힌트가 이분탐색
파라메트릭이라고??? 이게??? 왜???
'''

def my_bisect(lo, hi):
    answer = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        cnt = count_m(mid)
        if cnt >= M:
            answer = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return answer

# 길이가 m인 윈도우(팩) 수
def count_m(mid):
    cnt = 0
    move = 0

    while mid + move <= N:
        # 같은 거 중복할때까지 전진
        visited = dict()
        for i in range(move, move + mid):
            # 중복시 다음 스타트 지점
            if cards[i] not in visited:
                visited[cards[i]] = i
            else:
                move = visited[cards[i]] + 1
                break
        # 반복문 후 else = 반복문 종료시 1회 실행
        else:
            cnt = cnt + 1
            move = move + mid

    return cnt
        

N, M = map(int, input().split())
cards = list(map(int, input().split()))

# 카드팩 최소, 최대 크기
lo = 1
hi = N//M
print(my_bisect(lo, hi))

'''
감상(고전분투)

1. 
count_m 구축은 보다시피 안될때마다 다시 구축했음
visited set썼다가, next란 좌표 썼다가 요거 썼다가... 솔직히 개선점 많을 거 같은데 어딘지는 모르겠음
2. 
hi = mid - 1 저거 찾느라 한세월 걸림

파라메트릭으로 진짜 풀리긴 하는데 워메...
'''