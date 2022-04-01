'''
둘로 나누고 더하고.. 어디서 본거 같은데
'''
import sys
input = sys.stdin.readline

res = [987654321, -987654321]


def count_odds(x):
    cnt = 0
    for char in x:
        if char in '13579':
            cnt += 1
    return cnt


def dfs(x, cur):
    if len(x) == 1:
        res[0] = min(count_odds(x) + cur, res[0])
        res[1] = max(count_odds(x) + cur, res[1])
        return

    elif len(x) == 2:
        dfs(str(int(x[0]) + int(x[1])), cur + count_odds(x))

    else:
        odds = count_odds(x)
        for i in range(1, len(x) - 1):
            for j in range(i + 1, len(x)):
                dfs(str(int(x[:i]) + int(x[i:j]) + int(x[j:])), cur + odds)

# 문자열인체로 체크
x = input().rstrip()
dfs(x, 0)
print(*res)
