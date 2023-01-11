# 카페 확장
# 뭔 짓을 해도 시간은 100만 미만 = 매초 계산해도 될 거 같은데 그렇게는 안하고요.
# 사람 들어온 시점만 체크해도 됩니다.
def solution(menu, order, k):        
    N = len(order)
    
    # 누적합 비슷하게
    sums = [0]
    for i in range(N):
        next = sums[-1]
        if next < i*k:
            next = i*k
        sums.append(next+menu[order[i]])
    print(sums)
        
    idx = 0  # sumsIdx, 그 시간까지 받아간 사람 수가 될 예정
    time = 0
    answer = 1
    
    for i in range(1, N):
        time += k
        
        # 그 시간까지 받아간 사람 수        
        while idx != N and sums[idx+1] <= time:
            idx += 1

        answer = max(answer, i+1 - idx)

    return answer

# 3
# print(solution([5, 12, 30], [1, 2, 0, 1], 10))

# 4
# print(solution([5, 12, 30], [2, 1, 0, 0, 0, 1, 0], 10))

# 1
# print(solution([5], [0, 0, 0, 0, 0], 5))

print(solution([5, 12, 30], [1, 2, 0, 1], 3))