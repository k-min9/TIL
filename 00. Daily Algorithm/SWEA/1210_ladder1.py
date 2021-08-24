import sys
sys.stdin = open('input.txt')


def chk(x, y):
    if x >= 1 and boxes[y][x-1] == 1:
        # 좌측 이동
        while boxes[y][x-1] == 1:
            x = x - 1
            if x == 0:
                return 0
        return x
    elif x <= 98 and boxes[y][x+1] == 1:
        # 우측 이동
        while boxes[y][x+1] == 1:
            x = x + 1
            if x == 99:
                return 99
        return x
    return x


for _ in range(10):
    t = int(input())

    boxes = []
    for _ in range(100):
        boxes.append(list(map(int, input().split())))

    # for box in boxes:
    #     print(*box)

    # 골 찾기
    x = 0
    for i in range(100):
        if boxes[99][i] == 2:
            x = i
    y = 99

    # 99번 전진 (전진 후 탐색)
    for _ in range(99):
        y = y - 1
        x = chk(x, y)

    print(f'#{t }', x)
