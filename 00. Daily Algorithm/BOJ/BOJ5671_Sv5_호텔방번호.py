'''
접근 : 
itertools 써먹는 쪽이 힘들것 같으면 바로 dfs
를 하려고 했는데 나쁜 버릇이 나오는게 참 ㅎㅎ
'''
import sys
from collections import Counter
input = sys.stdin.readline

while True:
    try:
        N, M = map(int, input().split())
        answer = 0
        while N<=M:
            if Counter(str(N)).most_common(1)[0][1] == 1:
                answer += 1            
            N += 1
        print(answer)
    except:
        break

'''
다른 풀이 봤는데
testcase = sys.stdin.read().split("\n") 를 쓰면 
While True Try except 안 써도 된다고 한다. 
이거 말고 line 어쩌고 하나 더 있는거로 기억하는데
가장 건실한 풀이는 누적합이었다.
'''