'''
N보다 크면서 5를 적어도 K번 포함하는 가장 작은 수
(이게 좀 애매함 -> 최초 5 갯수 확인하면서 +) 작은 숫자부터 더하면...?
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
N += 1

N_list = list(str(N))
cur_idx = -1
max_idx = len(N_list)
while True:
    if N_list.count('5') >= K:
        break
    while N_list[cur_idx] == '5' and abs(cur_idx) < max_idx:
        cur_idx -= 1
    
    cur_value = int(''.join(N_list))
    cur_value = cur_value + 10 ** (abs(cur_idx)-1)
    N_list = list(str(cur_value))
    max_idx = len(N_list) # 문자열 길이가 더 길어지는지 체크

print(''.join(N_list))

'''
하다가 몇 번 막혀서 봤는데
이걸 문자열 -> 리스트로 만들생각을 하네
이러면 진짜 식이 깔끔해지고 최초 5 계산과 예외 걱정 확 줄일 수 있음
'''
