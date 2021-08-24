import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    print(f'#{t + 1}')

    # 스택의 스택 생성
    answers = [[1]]
    while True:

        answer = answers.pop()
        print(*answer)
        t -= 1
        if t + 1 == 0:
            break

        # 스택에 넣을 스택 작성
        next = list()
        next.append(1)
        for i in range(len(answer)-1):
            next.append(answer[i]+answer[i+1])
        next.append(1)

        # 만든 스택을 스택에 장전
        answers.append(next)


