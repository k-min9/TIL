'''
그리디하게 전진하면서 최저 기름값 나오면 갱신
그리고 최저 기름 값을 계속 충전하면서 한칸씩 전진하면 뭐 끝이다.
'''
import sys
input = sys.stdin.readline

N = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = prices[0]
answer = 0
for i in range(N-1):
    if min_price > prices[i]:
        min_price = prices[i]
    answer += (min_price * roads[i])
    
print(answer)
