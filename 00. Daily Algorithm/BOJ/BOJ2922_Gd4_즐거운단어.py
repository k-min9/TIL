'''
모음, 자음, L로 세상을 나누자.
견적 : 3^10(밑줄의 개수) = 6만 정도.
완전 탐색하고, 백트래킹 필요 없음
'''
import sys
input = sys.stdin.readline

# 상수(모음, 자음)
mother = {'A', 'E', 'I', 'O', 'U'}
son = {'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'}

def check(str):
    str = ''.join(str)
    # L 포함 여부 및 변환
    if 'L' not in str:
        return False
    while 'L' in str:
        str = str.replace('L', 'B')

    # 체크
    if 'AAA' in str:
        return False
    if 'BBB' in str:
        return False

    return True

# _에 A 또는 B 또는 L 집어 넣기
# 검색 시작 위치, 현재 진입 횟수, 종류별 포인트 획득량
def dfs(idx, depth, point):
    if depth == K and check(words):
        global answer
        answer += point

    for i in range(idx, N):
        if words[i] == '_':
            # 모음 넣기
            words[i] = 'A'
            dfs(i, depth+1, 5 * point)
            words[i] = 'B'
            dfs(i, depth+1, 20 * point)
            words[i] = 'L'
            dfs(i, depth+1, point)
            words[i] = '_'


words = list(input().rstrip())
N = len(words)
K = 0 # 밑줄의 갯수

# 입력 변환
for i in range(N):
    if words[i] in mother:
        words[i] = 'A'
    elif words[i] in son:
        words[i] = 'B'
    elif words[i] == '_':
        K += 1

answer = 0
dfs(0, 0, 1)
print(answer)

'''
예외 없이 한번에 빡 통과해서 기분 좋았던 문제입니다!
'''