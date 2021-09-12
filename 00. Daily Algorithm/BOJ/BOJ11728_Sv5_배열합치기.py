import sys
input = sys.stdin.readline

N, M = input().split()

list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))

answers = list_1 + list_2
answers.sort()
print(*answers)