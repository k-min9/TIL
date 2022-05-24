'''
우홋 재밌어 보이는 문제
근데 시간이 없어서 복습 차원으로 읽고 끝남 ㅠ
https://chance0523.github.io/algorithm/2020/12/16/algorithm-%EB%8B%A8%EC%B6%95%ED%82%A4%EC%A7%80%EC%A0%95/
'''
import sys
input = sys.stdin.readline


def plus(c):
    if c.isupper():
        words.append(c)
        words.append(c.lower())  # 소문자도 넣어준다.
    else:
        words.append(c)
        words.append(c.upper())  # 대문자도 넣어준다.


words = []  # 단축키 리스트
for i in range(int(input())):
    sList = list(input().rstrip().split(' '))
    # 들어온 문자열 돌면서 체크

    flag = False
    for j in range(len(sList)):
        # 1번 조건. 단어의 첫 글자
        if sList[j][0] not in words:  # 단축키 설정 가능
            plus(sList[j][0])         # 대소문자 둘 다 추가하기
            temp = sList[j][0]        # 괄호 씌우기 위해 앞 글자 빼줌
            sList[j] = sList[j][1:]   # 앞 글자 빼기
            sList[j] = '[' + temp + ']' + sList[j]  # 괄호 씌우기
            flag = True
            break

    if flag:
        print(' '.join(sList))
        continue

    for j in range(len(sList)):
        # 2번 조건. 알파벳 하나씩 보기
        flag = False
        for k in range(len(sList[j])):
            if sList[j][k] not in words:  # 단축키 설정 가능
                plus(sList[j][k])         # 대소문자 둘 다 추가하기
                temp = sList[j][k]        # 괄호 씌우기 위해 글자 빼줌
                # 글자 빼고 괄호 씌워주고 합치기
                if k != len(sList[j])-1:
                    sList[j] = sList[j][:k] + \
                        '[' + temp + ']' + sList[j][k + 1:]
                else:
                    sList[j] = sList[j][:k] + '[' + temp + ']'
                flag = True
                break
        if flag:
            break
        
    print(' '.join(sList))