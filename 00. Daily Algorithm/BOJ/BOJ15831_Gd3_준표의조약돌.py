import sys
input = sys.stdin.readline

# 총 돌 수, 검은 돌 B개 이하, 흰색 W 이상 최대한 길게
N, B, W = map(int, input().split())
rocks = input().rstrip()

left = 0
cnt_w = 0
cnt_b = 0
answer = 0
for right in range(N):
    # 검은색이 B개가 될때까지 우 포인터 전진
    if rocks[right]=='W':
        cnt_w += 1
    else:
        cnt_b += 1
        # 검은색 B-1개 될때까지 좌 포인터 전진
        while cnt_b > B:
            if rocks[left]=='W':
                cnt_w -= 1
            else:
                cnt_b -= 1
            left += 1

    if cnt_w >= W:
        answer = max(answer, right-left+1)
print(answer)