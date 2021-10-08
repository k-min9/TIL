'''
DFS로 브루트하게 싹 밀면 될거 같은데
'''
import sys
input = sys.stdin.readline


def dfs(N, sums):
    if N == 2:
        global answer
        answer = max(answer, sums)
        return
    
    for i in range(1, N-1): 
        tmp = energy[i]
        sum_plus = energy[i-1]*energy[i+1]
        
        del energy[i]
        dfs(N-1, sums + sum_plus)
        energy.insert(i, tmp)


answer = 0
N = int(input())
energy = list(map(int, input().split()))
dfs(N, 0)
print(answer)


'''
deque도 삭제, 삽입이 O(N)이라는 stack overflow 게시글을 보았다.
그럼 이거 각잡고 할거면 링크드 리스트 클래스를 직접 구현해야겠네!
'''