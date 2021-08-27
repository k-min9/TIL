import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for t in range(T):
    # 화덕 크기, 피자 개수
    N, M = map(int, input().split())
    # 치즈의 양
    Ci = list(map(int, input().split()))

    # 화덕 조와 대기 조
    pizzas = deque(range(N))
    Ci_idx = 0

    while len(pizzas) != 1:
        pizza = pizzas.popleft()
        Ci[pizza] = Ci[pizza]//2
        if Ci[pizza] != 0:
            pizzas.append(pizza)
        elif Ci_idx + N < M:
            pizzas.append(N + Ci_idx)
            Ci_idx += 1

    print(f'#{t+1}', pizzas[0] + 1)
