'''
문자열 검색, KMP 알고리즘
알기 쉬운 설명 : https://hooongs.tistory.com/304
'''
# 검색 대상, 검색어
def kmp(parent, pattern):

    n = len(parent)
    m = len(pattern)
    table = [0] * m  # 접두사, 접미사 정보 담기
    j = 0

    # 테이블 만들기
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            # 이전에 맞은 부분까지 돌아가서 비교
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    # 찾기
    j = 0
    count = 0
    loc = []
    for i in range(n):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1]
        if parent[i] == pattern[j]:
            if j == (m - 1):
                count += 1
                loc.append(i - m + 2)
                j = table[j]
            else:
                j += 1

    # 나타나는 횟수, 위치
    print(count) 
    print(*loc)


t = input()
p = input()
kmp(t, p)
