import sys
input = sys.stdin.readline

for t in range(int(input())):
    J, N = map(int, input().split())
    boxes = list()
    for _ in range(N):
        r, c = map(int, input().split())
        boxes.append(r*c)
    boxes.sort(reverse=True)

    cnt = 0
    for i in range(N):
        cnt += boxes[i]
        if cnt >= J:
            print(i+1)
            break