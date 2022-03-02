'''
트리의 독립집합.
뭔가 되게 카카오 같은 문제
그 노드를 선택하냐 안하냐는 방식으로 작업하면 될 것 같다.
dp[X][0] : 자기자신(X)을 포함하였을때 
dp[X][1] : 포함하지 않았을때의 값 > 자식들 중 큰 0 or 1 값을 더한다.
'''
import sys
input = sys.stdin.readline


def dfs(start):
    visit[start] = True
    dp[start][0] = w[start]
    num[start][0].append(start)
    for i in graphs[start]:
        if not visit[i]:
            # 끝까지 가서 밑에서 올라와야 빠지는 게 없다.
            dfs(i)
            # dp[X][0] 정산 중
            dp[start][0] += dp[i][1]
            for j in num[i][1]:
                num[start][0].append(j)
                
            # dp[X][1] 정산 중
            if dp[i][1] >= dp[i][0]:
                dp[start][1] += dp[i][1]
                for k in num[i][1]:
                    num[start][1].append(k)
            else:
                dp[start][1] += dp[i][0]
                for k in num[i][0]:
                    num[start][1].append(k)


N=int(input())
w = [0] + list(map(int, input().split()))

graphs = [[] for _ in range(N+1)]
dp = [[0] * 2 for _ in range(N+1)]
visit = [False for _ in range(N+1)]
num = [[[], []] for _ in range(N+1)]  # 선택 노드 기록


for i in range(N-1):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

dfs(1)

if dp[1][0] >= dp[1][1]:
    print(dp[1][0])
    a = num[1][0]
    a.sort()
    print(*a)
else:
    print(dp[1][1])
    a = num[1][1]
    a.sort()
    print(*a)
