import sys
sys.stdin = open('input.txt')

# 상수
chi = {'012', '123', '234', '345', '456', '567', '678', '789'}


def check(cards):
    # 같은 것 3개
    for card in cards:
        if cards.count(card) >= 3:
            return True
    # 연속된 세 개
    cards = ''.join(sorted(list(map(str, set(cards)))))
    for c in chi:
        if c in cards:
            return True
    return False


for tc in range(int(input())):
    # 카드
    cards = list(map(int, input().split()))
    # 일단 두장 씩 받고,
    players = [[cards[0], cards[2]], [cards[1], cards[3]]]

    # play the game
    answer = 0
    for i in range(4, 12):
        players[i % 2].append(cards[i])
        if check(players[i % 2]):
            answer = i % 2 + 1
            break

    print(f'#{tc+1}', answer)
