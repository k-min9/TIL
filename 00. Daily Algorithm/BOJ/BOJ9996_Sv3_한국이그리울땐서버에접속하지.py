'''
문자열, 정규식!
'''
import sys
import re
input = sys.stdin.readline

n = int(input())
s, e = input().rstrip().split("*")  # 첫문자 끝문자 체크
pattern = re.compile(s+".*"+e+"+")  # 표현식으로 변경 + 저장

for i in range(n):
    string = input().rstrip()
    a = pattern.search(string)  # 패턴 일치 확인
    if a and a.group() == string:
        print("DA")
    else:
        print("NE")
