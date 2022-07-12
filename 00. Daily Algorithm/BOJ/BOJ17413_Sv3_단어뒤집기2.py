'''
괄호 만나면 닫힐때까지 가기만 해도 음...
행동원칙 세우면 될 듯
< : 기존 쌓아놓은거 뒤집기, 쌓기 모드 중지
' ' : 기존 쌓아놓은거 뒤집기
> : 쌓기 모드 재개

끝?
'''
import sys
input = sys.stdin.readline

words = list(input().rstrip())

# 진행 인덱스와 뒤집을 범위의 시작 인덱스
i = 0
start = 0

while i < len(words):
    if words[i] == "<":
        i += 1 
        while words[i] != ">":
            i += 1 
        i += 1 
    # 숫자나 알파벳인지 애초에 in abcd... 같은게 취향
    elif words[i].isalnum():
        start = i
        while i < len(words) and words[i].isalnum():
            i+=1
        # 뒤집기
        words[start:i] = words[start:i][::-1]
    else:
        i+=1

print("".join(words))
