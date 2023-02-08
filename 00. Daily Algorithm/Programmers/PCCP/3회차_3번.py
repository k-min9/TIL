MOD = 1000000007

def solution(n, walls):
    answer = 1
    routes = [{1, 2} for _ in range(n)]

    for r, c in walls:
        # 2행 1열
        if r == 2 and c == 1:
            if 2 in routes[0]:
                routes[0].remove(2)
        # 2행 2열
        elif r == 2 and c == 2:
            if 2 in routes[0]:
                routes[0].remove(2)
            if 2 in routes[1]:
                routes[1].remove(2)
        else:
            if r in routes[c-3]:
                routes[c-3].remove(r)
            if r in routes[c-2]:
                routes[c-2].remove(r)
            if r in routes[c-1]:
                routes[c-1].remove(r)
    for i in range(n-1):
        answer = (answer * len(routes[i])) % MOD
        if answer == 0:
            break

    return answer