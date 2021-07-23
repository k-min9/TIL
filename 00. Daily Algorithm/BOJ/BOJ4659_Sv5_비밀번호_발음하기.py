'''
감상 : 아침부터 아이큐 테스트
vowelFlag 하나 세우고 바뀌면, 초기화.
e랑 o는 2점 나머지는 3점, 7점 이상이면 아웃.
사용 함수 : isvowel 
'''
import sys
input = sys.stdin.readline #210723 오늘부터 pragama 4996 급으로 뇌 비우고 고정하기로 했다.

#초기 세팅
set1 = ['a', 'e', 'i', 'o', 'u'] #islower, isalpha, isvowel 난 그런거 모름
set2 = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

#실행
case = input().rstrip()
#if문 안쓰고 초기화 했는데 나중에 왜 이리 썼는지 까먹고 5초 있다가 '아ㅡ'하는 녀석임
vowelFlag = case[0] in set1


while(case != 'end'):
    count = 0 #7점 이상이면 아웃
    lastword = ''
    vowelBomb = 999 #끝까지 999면 아웃 (모음 보유 체크)

    for char in case:

        if char in set1: #모음체크
            if not vowelFlag: #기존에 자음
                count = 0 #초기화
                vowelFlag = True

            if char =='e' or char == 'o':
                count = count + 2
            else:
                count = count + 3
            vowelBomb = 1

        elif char in set2: #자음 체크
            if vowelFlag: #기존에 모음
                count = 0 #초기화
                vowelFlag = False
            count = count + 3
        else:
            count = 999 #아웃!

        if lastword != char: #같은 글자 체크
            lastword = char
        elif lastword == 'e' or lastword == 'o':
            pass #eee ooo는 점수에서 걸림
        else:
            count = 999 #아웃!

        #아웃!이면 즉시 짐 싸자
        if count>=7:
            break
    
    count = count*vowelBomb

    if count>=7:
        print('<' + case + '> is not acceptable.')
    else:
        print('<' + case + '> is acceptable.')

    case = input().rstrip()

'''
감상 : 
해야될일을 한게 아니라 하고싶은일을 한 장난 가득한 풀이
그치만... 즐거운 시간 보내라고 했는걸...
p.s.
Flag를 Falg로 오타내고 못 찾고 있었다.
발음하기 쉬운 글자 ㄷㄷㄷ
'''




    


