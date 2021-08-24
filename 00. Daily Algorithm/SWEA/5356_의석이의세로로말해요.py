import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    words = list()
    for _ in range(5):
        word = input().rstrip()
        n = len(word)
        # 길이 15로는 절 막을 수 없습니다.
        word = word + ('#' * (15-n))
        words.append(word)
    # zip zip
    words = list(map(list, zip(*words)))
    words = sum(words, [])
    words = ''.join(x for x in words if x != '#')

    print(f'#{t+1}', words)
