'''
일부 비밀번호를 알 때 나머지...
수학문제 같네. 일단 7자리면 견적상 브루탈하게 풀어도 문제는 없어보인다. 일단은
'''
import sys
input = sys.stdin.readline


def dfs(length):
    if length == N:
        if sum(visited) == 0:
            global answer
            answer += 1
        return
    
    for i in range(10):
        if visited[i] >= 1:
            visited[i] -= 1
            dfs(length+1)
            visited[i] += 1
        else:
            dfs(length+1)

# 입력
# 비밀번호 길이, 비밀번호 들어가는 수
N, M = map(int, input().split())  
nums = list(map(int, input().split()))

answer = 0
visited = [0]*10
for num in nums:
    visited[num] += 1

dfs(0)
print(answer)

'''
되네 역시, 브루탈
'''
