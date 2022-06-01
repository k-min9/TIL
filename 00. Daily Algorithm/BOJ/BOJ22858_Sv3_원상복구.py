'''
...선형대수학?
'''
import sys
input = sys.stdin.readline

# 카드 개수 , 섞은 횟수
N, K = map(int, input().split())
cards_after = list(map(int, input().split()))  # 섞은 후
D = list(map(int, input().split()))  # 섞는 로직

# 순서까지 넣어서
D2 = list()
for i in range(N):
    D2.append([D[i], i])
D2.sort()

ans = [cards_after[i] for i in range(N)]
for i in range(K):
    temp = []
    for d in D2:
        temp.append(ans[d[1]])
    for j in range(N):
        ans[j] = temp[j]
print(*ans)