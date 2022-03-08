'''
최고 자식 노드 수 + 그 리프 노드 수 아니려나??
>>> [child_t[i]+i+1 for i in range(len(child_t))] 홀리 ㅋㅋㅋㅋㅋ
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
graphs = [[] for _ in range(N)]

for idx in range(1, N):
    graphs[nums[idx]].append(idx)

time = [0] * N

def dfs(x):
    child_t = []
    for next in graphs[x]:
        dfs(next)  # Leaf까지 내려가고 bottom up
        child_t.append(time[next])  # 시간 모음
    if not graphs[x]:
        # Child가 없으면 0
        child_t.append(0)

    child_t.sort(reverse=True)
    # 시간이 오래 걸리는 쪽부터 먼저 전화를 돌리기
    need_time = [child_t[i]+i+1 for i in range(len(child_t))]
    time[x] = max(need_time)
    
dfs(0)
print(time[0] - 1) # -1 : 루트노드 제외