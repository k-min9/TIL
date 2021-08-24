import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    boxes = list()
    for _ in range(N):
        boxes.append(list(map(str, input().split())))

    answers = [[] for i in range(N)]
    # 90도
    boxes = list(zip(*boxes[::-1]))
    for i in range(N):
        answers[i].append(''.join(boxes[i]))
    # 1800도
    boxes = list(zip(*boxes[::-1]))
    for i in range(N):
        answers[i].append(''.join(boxes[i]))
    # 270도
    boxes = list(zip(*boxes[::-1]))
    for i in range(N):
        answers[i].append(''.join(boxes[i]))

    print(f'#{t+1}')
    for answer in answers:
        print(*answer)
