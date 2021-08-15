'''
같은 스터디원 풀이를 봐버려서 다른 방법으로 못 풀겠음...
1. 자체가 펠린드롬
1-1. 하나 빼도 팰린드롬 => -1 (예시 zzzzz)
1-2. => 하나 뺀 값
2. 자체가 팰린드롬이 아님 => 문자열 길이
'''

def is_pal(str):
    return str == str[::-1]

string = input()

if is_pal(string):
    if is_pal(string[:-1]):
        print(-1)
    else:
        print(len(string)-1)
else:
    print(len(string))

'''
이거 한, 두 줄로 적을 수 있을거 같은데
'''