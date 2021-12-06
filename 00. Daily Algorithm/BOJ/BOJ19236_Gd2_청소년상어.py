'''
DFS백트래킹으로 기존 상태 돌아갈때 copy를 사용
물고기 마리수가 아니고 번호의 최대 합
'''
from copy import deepcopy
import sys
input = sys.stdin.readline

# 상수 : 이동 (주어진 정보대로 반시계 45도 이동하며 한바퀴, (y, x))
MOVES = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)]


def backtrack(shark_pos, maps, score, fish_info):
    global answer

    # 이동한 위치에 맞게 정보 갱신
    ny, nx  = shark_pos
    fish_caught = maps[ny][nx][0]  # 잡힌 물고기 번호
    shark_dir = maps[ny][nx][1]  # 다음 이동 방향
    
    # 먹힌 물고기 정리
    fish_info.pop(fish_caught)
    maps[ny][nx] = [0, None]

    # 물고기들 이동
    for fish_num in range(1, 17):
        if fish_num not in fish_info:
            continue
        y, x = fish_info[fish_num]

        # 방향 설정
        can_move = False
        for _ in range(9):
            dy, dx = MOVES[maps[y][x][1]]
            ny_fish, nx_fish = y+dy, x+dx
            # 이동 가능 조건
            if 0<=ny_fish<4 and 0<=nx_fish<4 and 0 <= maps[ny_fish][nx_fish][0] <= 16 and (ny_fish, nx_fish) != (ny, nx):
                can_move = True
                break
            else:
                maps[y][x][1] = (maps[y][x][1] + 1) % 8
        
        # 그래서 이동함?
        if not can_move:
            continue

        # 이동 - 비어있음
        if maps[ny_fish][nx_fish][0] == 0:
            maps[ny_fish][nx_fish] = maps[y][x]
            fish_info[fish_num] = (ny_fish, nx_fish)
            maps[y][x] = [0, None]
        # 이동 - 물고기 있어서 자리변경
        else:
            fish_tmp = maps[ny_fish][nx_fish][0]  # 기존 물고기 번호
            maps[ny_fish][nx_fish], maps[y][x] = maps[y][x], maps[ny_fish][nx_fish]
            fish_info[fish_num] = (ny_fish, nx_fish)
            fish_info[fish_tmp] = (y, x)

    # 상어 이동 가능 좌표
    ny, nx = ny + MOVES[shark_dir][0], nx + MOVES[shark_dir][1]

    # 다음 좌표로 이동
    while 0<= ny < 4 and 0<= nx < 4:
        # 물고기 있으면 dfs
        if maps[ny][nx][0] != 0:
            backtrack([ny, nx], deepcopy(maps), score + fish_caught, deepcopy(fish_info))
        
        # 계속 이동
        ny, nx = ny + MOVES[shark_dir][0], nx + MOVES[shark_dir][1]
    
    # 이동 끝났음. 최댓값 갱신
    answer = max(answer, score + fish_caught)
    return

# 기본 지도(번호, 방향)
maps = [[(0,0) for _ in range(4)] for _ in range(4)]
fish_info = dict()  # 물고기 번호당 좌표 기록

# 입력
x, y = 0, 0
for _ in range(4):
    # 입력 정보 : 번호, 방향, 번호, 방향, ...
    tmp = list(map(int, input().split()))
    for i in range(0, 8, 2):
        fish_num, fish_dir = tmp[i], tmp[i+1] - 1  # 시멘틱하게 굳이 언급, 차후 사용 없음
        maps[y][x] = [fish_num, fish_dir]
        fish_info[fish_num] = (y, x)
        x += 1
    y += 1
    x = 0

answer = 0

backtrack([0, 0], maps, 0, fish_info)
print(answer)
