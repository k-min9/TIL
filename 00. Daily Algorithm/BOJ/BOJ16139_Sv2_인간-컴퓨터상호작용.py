'''
대놓고 2차원 누적합이긴한디...
알파벳 숫자 변환말고 조금 똑똑한 방법 읎나? dict?
'''
import sys
input = sys.stdin.readline
from collections import defaultdict

strings = input().strip()
N = len(strings)
nums = defaultdict(list)
for alpha in 'abcdefghijklmnopqrstuvwxyz':
    cnt = 0
    nums[alpha].append(0)
    for i in range(N):
        if strings[i] == alpha:
            cnt += 1
        nums[alpha].append(cnt)

for _ in range(int(input())):
    alpha, l, r = map(str, input().split())
    l = int(l)
    r = int(r)
    print(str(nums[alpha][r+1] - nums[alpha][l]))

'''
파이써닉한게 정말 맘에 드는 풀이!
'''