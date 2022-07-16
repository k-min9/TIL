'''
제목이 어그로 쩌넼ㅋㅋ
'''
import sys
input = sys.stdin.readline

# 수열 길이, 질문 갯수
N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

pNum = [0]  # 누적합 용
for a in A:
    pNum.append(pNum[-1] + a)

for _ in range(Q):
    L, R = map(int, input().split())
    print(pNum[R] - pNum[L-1])
