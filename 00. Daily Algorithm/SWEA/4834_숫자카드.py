import sys
sys.stdin = open('input.txt')

from collections import Counter

T = int(input())
for t in range(1, T+1):
    N = int(input())
    cards = []
    for card in input():
        cards.append(int(card))

    cards.sort(reverse=True)
    answer = Counter(cards).most_common()

    # print(answer)

    print(f'#{t}', answer[0][0], answer[0][1])
