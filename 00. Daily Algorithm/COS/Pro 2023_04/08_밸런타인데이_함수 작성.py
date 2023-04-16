'''
구현. 참고로 답 더럽게 못짬
'''
def solution(dates):
    answer = 0
    for date in dates:
        chk = True
        for d in date:
            if d in "1248/":
                chk = False
        if chk:
            answer += 1

    return answer
