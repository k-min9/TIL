'''
DP. 3색이니까 마지막이 X색인 DP 3개를 운영하면 될 것 같은데
'''
import sys
input = sys.stdin.readline

N = int(input())
price = []

for _ in range(N):
    price.append(list(map(int, input().split())))


for i in range(1,N):
    price[i][0] = min(price[i-1][1], price[i-1][2]) + price[i][0]  # R
    price[i][1] = min(price[i-1][0], price[i-1][2]) + price[i][1]  # G
    price[i][2] = min(price[i-1][0], price[i-1][1]) + price[i][2]  # B

print(min(price[N-1]))

'''
되네
'''