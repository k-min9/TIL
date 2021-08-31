'''
1a+0b 0a+1b 1a-1b -a+2b 2a-3b -3a+5b 5a-8b
N = 30000까지
일단 피보나치 같은 느낌으로 전개되는건 알겠음.
N이 적으니 무식하게 전개해보고 막히면 거기서부터 체를 치고 범위를 좁히자
'''
import sys
input = sys.stdin.readline


N = int(input())
# 일단 두번째 수가 N//2 보다 작으면 최대 개수는 안나온다.
answer = 3
answers = list()
for b in range(N//2,N+1):
    tmp = [N, b, N-b]
    tmp_len = 3
    next = 2 * b - N
    while next >= 0:
        tmp_len = tmp_len + 1
        tmp.append(next)
        next = tmp[-2] - tmp[-1]

    if answer < tmp_len:
        answer = tmp_len
        answers = tmp[:]

print(answer)
print(*answers)

'''
여유!
'''