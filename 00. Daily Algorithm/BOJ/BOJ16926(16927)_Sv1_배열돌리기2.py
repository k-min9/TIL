'''
부딪히면 꺾는것도 신념임 ㄹㅇ루.
달팽이팽이로 풀어보자. 배열돌리기2는 R만 커졌다. 솔직히 상관없다.
'''

def rotate(border, left, right, up, down):
    # 시작지점(ex- 0,0,우측)
    x = border
    y = border
    dir = 0

    # 껍데기 규모로 계산시, if 횟수 감소
    while True:
        x += moves[dir][0]
        y += moves[dir][1]
        # 충돌
        if x == left or x == right or y == up or y == down:
            # 충돌했는데 이미 세번 꺾음
            if dir == 3:
                return None
            else:
                # 빠꾸!
                x -= moves[dir][0]
                y -= moves[dir][1]
                # 전진!
                dir += 1
                x += moves[dir][0]
                y += moves[dir][1]

        # 좌표설정 완료 + 이동한 곳에 있던거 keep
        graphs[border][border], graphs[x][y] = graphs[x][y], graphs[border][border]


# 상수 (하, 우, 상, 좌)
#moves = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 이거하면 정확히 역방향으로 간다.
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 배열 크기, 회전 수
N, M, R = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(N)]  # 쓰고보니 int변환 필요없었던거같은데

# 껍데기? 수
for border in range(min(N, M)//2):
    # 제자리로 돌아오는 회전 수 : 초기치(2*N+2*M-4) + 껍데기 안쪽으로 들어갈수록 8번 감소
    n = 2*N + 2*M - 4 - 8*border
    for _ in range(R%n):
        # 껍데기 횟수(?), 충돌 판정
        rotate(border, border-1, N-border, border-1, M-border)

for g in graphs:
    print(*g)

'''
이거 말고 밟으면 이동하는 포켓몬 장판 만들려고 했는데 배열돌리기2가 이렇게 풀래염
'''