import sys
sys.stdin = open('input.txt')


T = int(input())

names = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for t in range(T):
    trash, trash2 = input().split()
    words = list(input().split())
    answer = list()

    for word in words:
        for i in range(10):
            if names[i] == word:
                answer.append(i)
                break
    answer.sort()

    print(f'#{t + 1}')
    for a in answer:
        print(names[a], end=' ')
