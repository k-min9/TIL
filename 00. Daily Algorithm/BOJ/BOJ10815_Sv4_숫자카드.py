'''
set 넣고 돌리면 끝 아닌가 싶어서
면접전 가볍게 손풀기!
'''
import sys
input = sys.stdin.readline

n = int(input())
cards = set(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))

for query in queries:
    if query in cards:
        print(1, end = ' ')
    else:
        print(0, end = ' ')

'''
컨디션 올 그린!
'''