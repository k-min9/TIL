# 외톨이 알파벳
# string 길이 2600 = 맘대로 해라
def solution(input_string):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for a in alpha:
        chk = a+a
        while chk in input_string:
            input_string = input_string.replace(chk, a)

    chk_set = set()
    answer_set = set()

    for i in input_string:
        if i in chk_set:
            answer_set.add(i)
        else:
            chk_set.add(i)
    
    answers = list(answer_set)
    answers.sort()

    if answers:
        answer = ''.join(answers)
    else:
        answer = 'N'
    return answer

# "de"
print(solution("edeaaabbccd"))

# "e"
print(solution("eeddee"))

# "N"
print(solution("string"))

# "bz"
print(solution("zbzbz"))