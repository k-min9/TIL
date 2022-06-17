'''
아 고양이는 못참지~
투 포인터로 현재 들어가 있는 종류 수를 확인하면서 전진하고, 최종 max 값 꺼내면 끝
'''
import sys

input = sys.stdin.readline
N = int(input())
words = input().rstrip()
d = {}  # 딕셔너리

answer = 0
l = 0
for r in range(len(words)):
    d.setdefault(words[r], 0)
    d[words[r]] += 1
    while len(d) > N:
        d[words[l]] -= 1
        # 딕셔너리에서 제거
        if d[words[l]] == 0:
            del d[words[l]]
        l += 1
    answer = max(answer, r - l + 1)
print(answer)

'''
딕셔너리는 진짜 거의 만능
'''