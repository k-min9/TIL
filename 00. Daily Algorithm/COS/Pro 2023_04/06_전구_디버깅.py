'''
한줄 고치기
light[i] == 0을 light[i] != 0으로
'''
def solution(n, bulbs):
    answer = 0
    light = [0 for _ in range(11)]
    for i in range(len(bulbs)):
        light[bulbs[i]] = 1 - light[bulbs[i]]
    for i in range(1, n + 1):
        if light[i] != 0:
            answer += 1
    return answer
