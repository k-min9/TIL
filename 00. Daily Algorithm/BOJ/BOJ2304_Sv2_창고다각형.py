'''
투포인터 안 쓰고 스택 추천???
'''
import sys
input = sys.stdin.readline
N = int(input())


columns = [0] * 1001
for _ in range(N):
    idx, h = map(int, input().split())
    columns[idx] = h

l, r = 0, 1000
l_max, r_max = columns[l], columns[r]

answer = 0
while l<r:
    l_max, r_max = max(columns[l], l_max), max(columns[r], r_max)

    # 더 높은쪽으로 투포인터 이동
    if l_max <= r_max:
        answer += l_max
        l += 1
    else:
        answer += r_max
        r -= 1

answer += max(columns[l], columns[r])
print(answer)

'''
투포인터가 짱이징!
'''