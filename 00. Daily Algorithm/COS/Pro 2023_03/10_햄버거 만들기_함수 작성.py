'''
전부 탐색 그리드
'''
def solution(ingredient, k, s):
    answer = 0
    n = len(ingredient)
    last = (1 << n)
    for num in range(1, last):
        k_sum = 0
        s_sum = 0
        for idx in range(0, n):
            if (num & (1 << idx)) != 0:
                k_sum += ingredient[idx][0]
                s_sum += ingredient[idx][1]
        if k_sum <= k and s_sum >= s:
            answer += 1 
    return answer
