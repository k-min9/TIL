'''
5000글자 이하 문자열문제 = 파이썬 브루탈
'''
import sys
input = sys.stdin.readline


# 상수
word_set = ("c'", "j'", "n'", "m'", "t'", "s'", "l'", "l'", "d'", "qu'")

words = list(input().replace('-', ' ').split())

answer = len(words)
for word in words:
    if word.startswith(word_set):
        # 다음 글자 모음인지
        word_chk = word[word.index("'")+1]
        if word_chk in {'a', 'i', 'e', 'o', 'u', 'h'}:
            answer += 1

print(answer)


'''
반복문 없이, startswith(튜플이름)으로 빠르게 체크 가능
ㄴ 한번 틀림 : 프랑스어는 h도 모음이에요... : 본인의 상식을 믿지 말고 문제를 제대로 읽자
'''
