import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    words = input().rstrip()
    stack = list()

    for word in words:
        # 넣는 것과 맨 위 비교
        if stack and stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)

    print(f'#{t+1}', len(stack))
