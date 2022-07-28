'''
일단 음수인점 조심해서 하려고 했는데 N, K가 100? 
브루탈...?
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
card_share = list(map(int, input().split()))
card_team = set((map(int, input().split())))

for _ in range(K):
    s = -int(1e9)
    x = 0
    for i in card_team:
        for j in card_share:
            if s <= i*j:
                s = i*j
                x = i
    card_team.remove(x)

ans = -int(1e9)
for i in card_team:
    for j in card_share:
        ans = max(ans, i*j)

print(ans)
