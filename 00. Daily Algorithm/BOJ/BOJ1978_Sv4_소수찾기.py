'''
1000 이하면 필요 없긴한데 그냥 체 만들어서...
'''
import sys
input = sys.stdin.readline

# 체 만들기
is_prime = [1]* 1001
is_prime[0] = 0
is_prime[1] = 0
for i in range(2, int(1001**0.5)+1):
    if is_prime[i] == 1:
        for chk in range(2*i, 1001, i):
            is_prime[chk] = 0

# 출력
N = int(input())
answer = 0
for num in map(int, input().split()):
    answer += is_prime[num]
print(answer)