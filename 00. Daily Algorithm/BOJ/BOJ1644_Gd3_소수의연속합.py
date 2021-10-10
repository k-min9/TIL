'''
접근 : 누적합을 (n/2+1)보다 작은 모든 소수에 실행해서 DP하면 되는거 아닐까
'''
import sys
input = sys.stdin.readline

n = int(input())
primes_list = [1]*(n+1)
primes_list[0] = 0
primes_list[1] = 0
primes_sum = [0]

# 체치기
for i in range(2, int(n**0.5)+1):
    if primes_list[i] == 1:
        for j in range(2*i, n+1, i):
            primes_list[j] = 0
'''
1차 시도 실패 : 이게 시간 초과가 뜨네??
# 누적합(체를 그냥 n까지 치는게 이득일거 같지만, 이걸 n/2 + 1까지만 시행했으면 이게 더 이득)
for idx, i in enumerate(primes_list):
    if i == 1:
        primes_sum.append(primes_sum[-1]+idx)

s = len(primes_sum)
answer = 0
for i in range(s):
    for j in range(i+1,s):
        if primes_sum[j] - primes_sum[i] == n:
            answer += 1
        elif primes_sum[j] - primes_sum[i] < n:
            continue
print(answer)
'''
primes_number = list()
for i in range(2, n + 1):
    if primes_list[i]:
        primes_number.append(i)

primes_len = len(primes_number)
interval_sum = 0
right = 0
answer = 0
for left in range(primes_len):
    while interval_sum < n and right < primes_len:
        interval_sum += primes_number[right]
        right += 1

    if interval_sum == n:
        answer += 1
    interval_sum -= primes_number[left]

print(answer)

'''
2차 시도 : 투 포인터 = 통과
'''