'''
다들 이진 탐색을 생각했을거라고 생각한다.
근데 던젼 수가 123456이면 이거 dp로도 되는거 아닐까???
'''

import sys
input = sys.stdin.readline

# 전투 시 감소하는 체력 출력
def fight(atkH, atkM, hpM):
    return -((hpM - 1) // atkH) * atkM

# 포션 먹고 증가하는 체력
def heal(atkH, hpH, atkP, hpP):
    atkH = atkH + atkP
    hpH = min(0, hpH + hpP)
    return atkH, hpH

# 던젼 수 용사 공격력
N, atkH = map(int, input().split())

# 초기 용사 체력과 어디까지 내려갔나
hpH = 0
ans = 0

# 레츠 고 던전
for _ in range(N):
    room, atk, hp = map(int, input().split())
    if room == 1:  # 몬스터 던젼
        hpH = hpH + fight(atkH, atk, hp)
    else:  # 포션 방
        atkH, hpH = heal(atkH, hpH, atk, hp)
    ans = min(hpH, ans)
    # print('go', hpH, ans)

print(abs(ans)+1)

'''
하다보니 dp조차 필요 없었다. 아니 함수조차 필요 없었다.
제작자는 이진탐색을 염두하고 문제라는건 보이는데
문제는 던젼수가 너무 작아요 2천만개 이상 되어야 함
그쯤 가면 이진탐색에 필요한 용사체력이 하늘을 뚫어서 이것도 힘들듯
'''