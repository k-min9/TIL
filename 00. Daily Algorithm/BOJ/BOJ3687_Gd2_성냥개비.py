'''
정해진 성냥개비로 만들 수 있는 가장 큰, 작은 수
절대 안쓸것 같은 숫자도 있는디...?

사용 갯수, 숫자
2개:1, 3개:7, 4개:4, 5개:2,3,5, 6개:6,9,0, 7개:8
큰 수 : 자리수 크게, 작은 수 : 최대한 8 쓰기
'''
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    num = int(input())
    
    answer_max = '7' * (num % 2) + '1' * (num // 2 - (num % 2))

    # 작은 수 구하기
    # x개로 만들 수 있는 가장 작은 수, 10개 까지
    answer = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]

    if num <= 10:
        answer_min = answer[num]
    else:
        answer_min = ''
        while True:
            if num >= 7:
                answer_min += '8'
                num -= 7
            else:
                break
        small = {2:'1', 5:'2', 6:'6'}
        if num in small:
            answer_min = small[num] + answer_min
        else:
            if num == 1:
                answer_min = '10' + answer_min[1:]
            elif num == 3:
                answer_min = '200' + answer_min[2:]
            elif num == 4:
                answer_min = '20' + answer_min[1:]
    print(answer_min, answer_max)    


