'''
슬라이딩 윈도우 . 문제만들려고 더럽게도 짰음
한 줄 고치기 : total >= t를 total > t로
'''

def solution(seminars, t):
    st = 0
    total = 0
    answer = 0
    for ed in range(len(seminars)):
        total += seminars[ed]
        while total > t:
            total -= seminars[st]
            st += 1
        if total == t:
            answer += 1
    return answer
