'''
트리... 흠...
'''
import sys
input = sys.stdin.readline

N = int(input())
links = [0] * N
graphs = list()

for _ in range(N-1):
    a, b = map(int, input().split())
    links[a-1] += 1
    links[b-1] += 1
    graphs.append((a,b))

answer_D, answer_G = 0, 0

# ㅈ 트리 구하기 (조합 C3)
for i in range(N):
    if links[i] >= 3:
        answer_G += links[i] * (links[i] - 1) * (links[i] -2 ) // 6

# ㄷ 트리 구하기
for a, b in graphs:
    answer_D += (links[a-1] -1) * (links[b-1] -1)

if answer_D > answer_G * 3:
    print("D")
elif answer_D < answer_G * 3:
    print("G")
else:
    print("DUDUDUNGA")

'''
DFS, BFS를 쓰면 시간, 메모리 초과하는 문제
‘트리 자체의 연결 구조’는 신경쓰지 않아도 되고,
단지 각 노드의 degrees만 알면 ㅈ트리는 조합으로, ㄷ트리는 두 노드의 degrees의 곱으로 바로 구할 수 있다.
'''