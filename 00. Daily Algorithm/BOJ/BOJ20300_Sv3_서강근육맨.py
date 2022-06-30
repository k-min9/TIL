'''
하루 최대 2개인데 합이 M 이하
'''
import sys
input = sys.stdin.readline

N = int(input())
weights = list(map(int,input().split()))
weights_list = list()  # 합산들의 합
weights.sort()

# 홀수개면 일단 제일 큰 것 하나 제거
if(N%2 == 1):
    weights_list.append(weights[-1])
    weights=weights[:-1]

for i in range(len(weights)//2):
        weights_list.append(weights[i] + weights[len(weights)-1-i])

print(max(weights_list))

'''
브1 정도인데...?
'''