import sys
sys.stdin = open('input.txt')


# 가위 바위 보
def rsp(left_idx, right_idx):
    # 최후의 하나까지 쪼개면 그 값
    if left_idx == right_idx:
        return left_idx
    mid = (left_idx + right_idx) // 2
    return fight(rsp(left_idx, mid), rsp(mid+1, right_idx))


# 이쪽이 진짜 가위바위보(b가 이기는 세가지 경우 제외하고 전부 a)
def fight(a, b):
    if (nums[a] == 1 and nums[b] == 2) or \
        (nums[a] == 2 and nums[b] == 3) or \
        (nums[a] == 3 and nums[b] == 1):
        return b
    return a


T = int(input())
for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    left = 0
    right = N - 1

    print(f'#{t+1}', rsp(0, N - 1) + 1)
