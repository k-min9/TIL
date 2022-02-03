'''
최소 필요동전수 -> 위에서 커트 친다?
'''
import sys
input = sys.stdin.readline

# 동전 종류와 만들어야 하는 가치
N, K = map(int, input().split()) 
coins = [int(input()) for _ in range(N)]

count = 0
for i in range(N-1, -1, -1):
    count += K//coins[i]
    K = K % coins[i]

print(count)


'''
Flask 하고 돌아온다!
'''