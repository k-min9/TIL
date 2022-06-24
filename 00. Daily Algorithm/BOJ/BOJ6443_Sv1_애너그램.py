'''
set이랑 itertools 합쳐서 끝내면 될거같은데...
'''
# import sys
# input = sys.stdin.readline
# from itertools import permutations

# N = int(input())
# words = [input().rstrip() for _ in range(N)]

# for word in words:
#     answers = set()
#     for comb in permutations(word, len(word)):
#         answers.add(''.join(comb))
    
#     answers = list(answers)
#     answers.sort()
#     for answer in answers:
#         print(answer)
'''
뭐 응.... 시간초과 >> words를 일단 재배열해보기
'''
# import sys
# input = sys.stdin.readline
# from itertools import permutations

# N = int(input())
# words = [input().rstrip() for _ in range(N)]
# answers = set()
# for word in words:
#     word = sorted(list(map(str, word)))
#     for comb in permutations(word, len(word)):
#         answer = ''.join(comb)
#         if answer not in answers:
#             answers.add(answer)
#             print(answer)
'''
통과 케이스는 늘었지만 결과적으로 시간초과해서 itertools 포기하고 평범하게 백트랙
'''
import sys
input = sys.stdin.readline


# 변수로 알파벳의 갯수
def backtrack(cnt):
    if cnt == len(word):
        print("".join(answer))
        return

    for k in visited:
        if visited[k]:
            visited[k] -= 1
            answer.append(k) 
            backtrack(cnt + 1)
            visited[k] += 1 
            answer.pop()

n = int(sys.stdin.readline())

for _ in range(n):
    word = sorted(list(map(str, input().strip())))
    visited = {}
    answer = []

    for i in word:
        if i in visited:
            visited[i] += 1
        else:
            visited[i] = 1

    backtrack(0)
