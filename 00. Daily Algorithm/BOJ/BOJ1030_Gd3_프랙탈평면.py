'''
견적 : 8^10 = 으어어...
전체 그래프 그리기 같은건 메모리도 시간도 확실히 터질테고, 똑똑한 풀이를 요구하는 문제다.
'''
import sys
input = sys.stdin.readline

#흰(0)인지 검(1)인지 확인 후 출력 
def is_black1(x, y):
    if x == 0 or y == 0:
        return print(0, end = "")
    if is_black2(x % N, y % N):
        return print(1, end = "")
    else:
        is_black1(x//N, y//N)
    
def is_black2(x, y):
    if black_start <= x < black_end and black_start <= y < black_end:
        return True
    else:
        return False


# 시간, 쪼개지는 횟수, 검정 비율, row, column
s, N, K, R1, R2, C1, C2 = map(int, input().split())

# 검은색 인덱스, 한 변의 길이
black_start = (N-K)//2
black_end = black_start + K
length = N ** s

for y in range(R1, R2+1):
    for x in range(C1, C2+1):
        is_black1(x, y)
    print()

'''
내! 재귀해서 분할정복했습니다!
견적은 2500(조사면적)*10(최대 재귀 횟수)
연산에서 재귀의 비율이 커서 pypy가 더 느림!
'''