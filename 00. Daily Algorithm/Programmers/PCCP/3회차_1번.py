# 일단 풀리기는 하는 방식
def solution(cards, n, flips):
    answer = [0]*n
    player = 0  # 현재 플레이어
    k = len(cards)//2
    pairs = [[] for _ in range(k)]
    for i in range(2*k):
        pairs[cards[i]-1].append(i+1)

    for flip in flips:
        if sorted(flip) in pairs:
            answer[player] += 1
        else:
            player = (player+1)%n


    return answer