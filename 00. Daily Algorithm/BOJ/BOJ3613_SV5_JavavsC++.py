'''
문자열 조작인가-
'''
import sys
input = sys.stdin.readline

words = input().rstrip()
# 첫글자 체크
if words[0].isupper():
    print('Error!')
    exit(0)
if words[0] == '_':
    print('Error!')
    exit(0)

answers = ''
# 1은 C++ 2는 자바
chartype = 0

# 다음 글자 upper 여부
flag = False
for i in range(len(words)):
    if flag:
        if words[i] == '_' or words[i].isupper():
            answers = 'Error!'
            break    
        else:
            answers = answers + words[i].upper()
            flag = False
    elif words[i].isupper():
        answers = answers + '_' + words[i].lower()
        # 자바 체크
        if chartype == 1:
            answers = 'Error!'
            break
        else:
            chartype = 2
    elif words[i] == '_':
        flag = True
        # C++ 체크
        if chartype == 2:
            answers = 'Error!'
            break
        else:
            chartype = 1
    else:
        answers += words[i]

if not flag:
    print(answers)
else:
    print('Error!')

'''
누덕누덕...
'''