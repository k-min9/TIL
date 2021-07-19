# 접근 : 15가 될 때 마다 3*5를 5*3으로 바꿔볼까
# 모든 정수를 3n+0 3n+5 3n+10로 분류

# 시작
Amt = int(input())


if Amt%3==0: #case 1 (최종 +0)
    Answer = Amt // 15 # 변환 단위 (3*5 to 5*3)
    Amt = Amt - Answer * 15
    Answer = (3 * Answer) + (Amt // 3)
elif Amt%3==2: #case 2 (최종 +1)
    Amt = Amt - 5
    if Amt <0:
        Answer = -1
    else:
        Answer = Amt // 15
        Amt = Amt - Answer * 15
        Answer = (3 * Answer) + (Amt // 3)
        Answer = Answer + 1
else: #case 3 (최종 +2)
    Amt = Amt - 10
    if Amt <0:
        Answer = -1
    else:
        Answer = Amt // 15
        Amt = Amt - Answer * 15
        Answer = (3 * Answer) + (Amt // 3)
        Answer = Answer + 2

print(Answer)        

