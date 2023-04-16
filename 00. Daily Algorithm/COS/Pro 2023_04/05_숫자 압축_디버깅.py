'''
디버깅 : num>10 을 num!=0 으로
'''
def solution(num):

    while (num >= 10):
        total = 0
        while num > 0:
            total += num % 10
            num = num // 10
        num = total

    return num
