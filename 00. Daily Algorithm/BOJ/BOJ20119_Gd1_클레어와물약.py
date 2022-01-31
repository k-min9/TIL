'''
가리키는 간선수 = 0 -> 유해브 디스 물약인 위상 정렬
'''
import sys
input = sys.stdin.readline


# 물약 종류 수, 레시피 수
N, M = map(int, input().split())
remain = []
outcome = []
recipes = [[] for _ in range(N+1)]
for i in range(M):
    k,*recipe,r = map(int,input().split())
 
    # 레시피 필요한 수
    remain.append(k)
    # 레시피 결과물
    outcome.append(r)
    # 레시피 내용물
    for num in recipe:
        recipes[num].append(i)

# 현재 보유 상황
L = int(input())
cur_potion = list(map(int,input().split()))
result = set(cur_potion)
 
 
while cur_potion:
    cur  = cur_potion.pop()
    for recipe_idx in recipes[cur]:
        remain[recipe_idx] -= 1
        if remain[recipe_idx] == 0 and outcome[recipe_idx] not in result:
            cur_potion.append(outcome[recipe_idx])
            result.add(outcome[recipe_idx])

result = sorted(list(result))
print(len(result))
print(*result)
