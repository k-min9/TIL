import sys
sys.stdin = open('input.txt')

for t in range(10):
    trash, passwords = input().split()
    stack = list()

    for password in passwords:
        # 넣는 것과 맨 위 비교
        if stack and stack[-1] == password:
            stack.pop()
        else:
            stack.append(password)

    print(f'#{t+1}', ''.join(stack))
