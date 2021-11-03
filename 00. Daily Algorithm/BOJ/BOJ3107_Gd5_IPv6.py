'''
문자열 조작 = 파이썬이 편함
'''
import sys
input = sys.stdin.readline

answers = input().rstrip().split(':')
answers_to_input = 8
for answer in answers:
    if answer != '':
        answers_to_input -= 1

# 규칙 2
if answers_to_input:
    for i in range(len(answers)):
        if answers[i] == '':
            answers = answers[:i] + ['0000'] * answers_to_input + answers[i:]
            break

# ' ' 제거
answers = ' '.join(answers).split()
print(answers)

# 규칙 1
for i in range(8):
    answers[i] = answers[i].zfill(4)

print(':'.join(answers))