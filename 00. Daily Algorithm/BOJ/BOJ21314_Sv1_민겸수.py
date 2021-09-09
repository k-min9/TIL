'''
접근 : K기준으로 자르는건 확정 M은 독립가능
발상 : 
K를 최대한 촘촘히 자름 = 작은 수 
K포함 최대한 크게 자름 = 큰 수 같은데??
'''
import sys
input = sys.stdin.readline

words = input().rstrip()

# 제일 큰 수
answer = ''
cnt = 0
for w in words:
    if w == 'K':
        answer = answer + '5' + '0' * cnt
        cnt = 0
    else:
        cnt += 1
answer = answer + '1'*cnt
print(answer)

# 제일 작은 수
while 'MM' in words or '0M' in words:
    words = words.replace('MM', 'M0')
    words = words.replace('0M', '00')

answer2 = words.replace('M','1').replace('K','5')
print(answer2)

'''
실버1 구현문제가 아닌데 얘는
'''