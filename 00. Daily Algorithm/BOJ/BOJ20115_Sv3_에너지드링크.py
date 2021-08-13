'''
최대힙?
'''

# 전처리
import sys
input = sys.stdin.readline

N = int(input())
q = list(map(int,input().split()))
q.sort()

answer = q.pop()
answer = answer + sum(q) / 2

print(answer)

'''
q는 최대힙 넣으려다가 만 흔적이고,
풀면서 ???가 멈추지 않았던 질문 이거 왜 실버임?
'''