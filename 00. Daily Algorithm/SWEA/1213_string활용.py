import sys
sys.stdin = open('input.txt', encoding='UTF8')


for t in range(10):
    trash = input().split()
    splits = input().split()
    answer = list(input().split(*splits))

    print(f'#{t + 1}', len(answer)-1)
