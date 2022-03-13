'''
해당 문자열을 K개 포함한 포함한 가장 짧은 연속 문자열
해당 문자열을 K개 포함한 가장 긴 연속 문자열(앞과 뒤가 해당 문자열)
문자열 길이 10000, 슬라이딩 윈도우를 각각의 단어에 시도하면 26회...?
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    # 문자열, 문자열 조건
    W = input().rstrip()
    K = int(input())

    N = len(W)

    answer_min = 10001
    answer_max = 0
    alphas = 'abcdefghijklmnopqrstuvwxyz'
    flag = False
    for alpha in alphas:
        if alpha in W and W.count(alpha) >= K:
            flag = True
            pos = -1
            pos_word = list()
            while True:
                pos = W.find(alpha, pos+1)
                if pos == -1:
                    break
                pos_word.append(pos)
            for j in range(0, len(pos_word)-K+1):
                length = pos_word[j+K-1] - pos_word[j]
                answer_max = max(answer_max, length)
                answer_min = min(answer_min, length)
    # 출력            
    if flag:
        print(answer_min+1, answer_max+1)
    else:
        print(-1)




