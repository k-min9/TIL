'''
역으로 소트하고 
적재량 큰것과 아닌것 1:1 대응하면서 내려가는것 반복하고 
반복 횟수를 적으면 될 것 같다.
'''
import sys
inpunt = sys.stdin.readline

# 입력 (크레인 / 상자)
N = int(inpunt())
crane = list(map(int, inpunt().split()))
M = int(inpunt())
box = list(map(int, inpunt().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

# 배로 옮길 수 없는 경우 => 제일 강한 크레인이 담을 수 없는 경우
if box[0] > crane[0]:  
    print(-1)
    sys.exit()
else:
    answer = 0
    while(True):
        # 박스 비울때까지 실행
        if not box: 
            break  
        for i in range(len(crane)):
            for j in range(len(box)):
                if crane[i] >= box[j]:
                    del box[j]
                    break
        # 1분간 할 수 있는 모든 작업 후, 체크
        answer += 1
    print(answer)